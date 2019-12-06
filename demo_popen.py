# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

if __name__ == '__main__':
    cmd = ['python', 'subprocess_run.py']
    process = Popen(cmd, stdin=PIPE)
    process.stdin.close()
    if process.wait() != 0:
        print("There were some errors")
