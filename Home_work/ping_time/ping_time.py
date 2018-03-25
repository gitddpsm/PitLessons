import os
import subprocess


def ping(address):
    return not os.system('ping %s -n 1' % (address,))

add_str = '8.8.8.8'
os.system('chcp 65001')
adbcd = subprocess.check_output(['ping',(add_str)])
print(adbcd)
