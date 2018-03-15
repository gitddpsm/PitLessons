# -*- coding: utf-8 -*-
import datetime
# import statvfs
import re
import logging
from logging.handlers import RotatingFileHandler
from argparse import ArgumentParser
import os
import os.path as osp


FILENAME_TIMESTAMP_RE = r"(?:\D|^)(\d{14})(?:\D|$)"
DISPATCHER_LOG_TIMESTAMP_RE = r'dispatcher_(\d{4}-\d{2}-\d{2})'

FILE_TYPES = [
    ("SLITFILE", r'(vp|raw)-slit.+jpg$', 5),
    ("AVIFILE", r'(.+avi$)', 1),
    ("INDUCTIONFILE", r'(_induction.+log$)', 1),
    ("LOGFILE", r'((?!_induction).+log$)', 5),
    ("XTFILE", r'(.-raw-xt_.)', 5),
    ("CORE", r'(^core$)', 1),
    ("DISPATCHER", r'^dispatcher_(\d{4}-\d{2}-\d{2})', 1),
    ("SENSORS", r'(.+ldj$)', 1),
    ("XMLFILE", r'.+xml$', 1),
]


def isEnoughtFreeSpace(desired_bytes):  # space in bytes
    st = os.statvfs('.')
    available_bytes = st.f_bavail * st.f_bsize
    return available_bytes >= desired_bytes


def guess_timestamp_by_filename(filename):
    filename = osp.basename(filename)
    m = re.search(FILENAME_TIMESTAMP_RE, filename)
    if m:
        return datetime.datetime.strptime(m.group(1), '%Y%m%d%H%M%S')
    m = re.search(DISPATCHER_LOG_TIMESTAMP_RE, filename)
    if m:
        return datetime.datetime.strptime(m.group(1), '%Y-%m-%d')


def file_define(name, path):
    now = datetime.datetime.now()

    date = guess_timestamp_by_filename(name)

    if re.search(DISPATCHER_LOG_TIMESTAMP_RE, name):
        date = datetime.datetime.fromtimestamp(
            os.stat(osp.join(path, name)).st_mtime
        )

    if not date:
        date = datetime.datetime.fromtimestamp(
            os.stat(osp.join(path, name)).st_mtime
        )

    age = (now - date).total_seconds()

    for tp in FILE_TYPES:
        if re.search(tp[1], name):
            temp = [osp.join(path, name), tp[0], age,
                    age / float(tp[2]), False]
            return temp
        else:
            temp = [osp.join(path, name), "OTHER", age, age / 3.0, False]

    assert temp
    return temp


def list_files_for_delete(levels, path='.', logpath=None):
    """
    we list from current directory, so `dirpath.count('/')` works
    """
    files = []

    for dirpath, dirnames, filenames in os.walk(path, followlinks=True):
        if logpath in dirnames:
            dirnames.remove(logpath)
        if dirpath.count('/') >= levels:
            for f in filenames:
                files.append(file_define(f, dirpath))

    files.sort(key=lambda age: age[3], reverse=True)
    return files


def remove_files_while_no_space(free, gen):
    for fi in gen:
        if isEnoughtFreeSpace(free):
            return True
        filename, filetype, _, normage, _ = fi
        try:
            os.remove(filename)
        except Exception as e:
            logging.error(e)
        logging.debug(normage, filename)
        fi[4] = True
    if isEnoughtFreeSpace(free):
        return True


def setup_logging(path):
    handler = RotatingFileHandler(path, maxBytes=32768, backupCount=5)
    formatter = logging.Formatter('%(levelname)s %(asctime)s  %(message)s',
                                  '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger = logging.getLogger("")
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(free_bytes, minage, target_dir, levels):
    os.chdir(target_dir)
    LOGPATH = 'cleanup'

    if not osp.exists(LOGPATH):
        os.mkdir(LOGPATH)
    setup_logging(osp.join(LOGPATH, 'cleanup.log'))

    lock_path = '/tmp/.cleanup.{:x}.lock'.format(hash(target_dir) & 0xffffffff)

    if osp.exists(lock_path):
        logging.info("Cleaning `{}` is in progress (lock file `{}` exists).\n"
                     .format(target_dir, lock_path))
        return
    if isEnoughtFreeSpace(free_bytes):
        logging.info("Don't need to clean `{}` - enough free space.\n"
                     .format(target_dir))
        return
    logging.info("Cleaning at `{}`".format(target_dir))
    with open(lock_path, 'a'):
        pass
    logging.info("{} CREATED".format(lock_path))

    try:
        st = os.statvfs(target_dir)
        spbefore = st.f_bavail * st.f_bsize

        logging.info("Free space before {:.0f} bytes".format(spbefore))

        listFilesForDelete = list_files_for_delete(levels, logpath=LOGPATH)

        old_files = (fi for fi in listFilesForDelete
                     if fi[2] > minage * 60 * 60)
        today_avi = (fi for fi in listFilesForDelete
                     if fi[2] <= minage * 60 * 60 if fi[1] == 'AVIFILE')
        today_files = (fi for fi in listFilesForDelete
                       if fi[2] <= minage * 60 * 60 if fi[1] != 'AVIFILE')

        for gen, msg in [(old_files, ""),
                         (today_avi, "avi "),
                         (today_files, "other ")]:
            logging.info("Start to clear {}files.".format(msg))
            if remove_files_while_no_space(free_bytes, gen):
                break

        types = {}
        for filename, filetype, age, normage, deleted in listFilesForDelete:
            if not deleted:
                if filetype not in types:
                    types[filetype] = (filename, filetype, age, normage)

        for filetype in sorted(types):
            age = types[filetype][2]
            logging.info("{}: {:.2f} hours".format(
                filetype, age / (60.0 * 60.0)))

        sa = os.statvfs(target_dir)
        spafter = sa.f_bavail * st.f_bsize

        logging.info("Free space after {:.0f} bytes".format(spafter))
        logging.info("Space freed: {:.0f} bytes".format(spafter - spbefore))

    finally:
        TWO_DAYS_AGO = datetime.datetime.now() - datetime.timedelta(days=2)
        for dirpath, dirnames, filenames in os.walk('.', followlinks=True):
            dir_date = guess_timestamp_by_filename(dirpath)
            if dir_date and dir_date > TWO_DAYS_AGO:
                continue
            if dirpath.count('/') > levels:
                try:
                    os.rmdir(dirpath)
                except OSError as e:
                    pass

        os.remove(lock_path)
        logging.info("{} DELETED\n\n".format(lock_path))


def parse_arguments():
    DEFAULT_TARGETPATH = '/home/avc/avc_output'
    DEFAULT_SKIP_LEVELS = 1
    BYTES_IN_GB = 1024 * 1024 * 1024
    p = ArgumentParser()
    p.add_argument('free_bytes', metavar='free',
                   type=lambda gb: int(float(gb) * BYTES_IN_GB),
                   help="total space that must be free, in Gb")
    p.add_argument('minage', type=float,
                   help="minimal age for files to leave untouched, in hours")
    p.add_argument('--target-dir', '-d', metavar='DIR',
                   default=DEFAULT_TARGETPATH,
                   help="clean this DIR, default `{}`"
                        .format(DEFAULT_TARGETPATH))
    p.add_argument('--skip-levels', '-l', dest='levels', metavar='N',
                   default=DEFAULT_SKIP_LEVELS, type=int,
                   help="Do not cleanup up to N levels, default = {}"
                        .format(DEFAULT_SKIP_LEVELS))
    return vars(p.parse_args())


if __name__ == '__main__':
    main(**parse_arguments())
