# -*- coding: utf-8 -*-
#TODO Красное на белом
# https://habrahabr.ru/post/117236/
import sys
import locale

print(sys.getdefaultencoding())
#ascii
print(locale.getpreferredencoding()) # linux
#UTF-8
print(locale.getpreferredencoding()) # win32/rus
#cp1251
# и самое интересное:
print(sys.stdout.encoding) # linux
#UTF-8
print(sys.stdout.encoding) # win32
#cp866

print(u"\x1b[31;40mЧто-то красное на белом\x1b[0m")


