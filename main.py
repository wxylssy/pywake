#! /usr/bin/python3

import datetime
import time
import os

def main():
    tm = input("唤醒时间（%Y-%m-%d %H:%M:%S）：")
    time.sleep(1)
    tm = datetime.datetime.strptime(tm, '%Y-%m-%d %H:%M:%S')
    seconds = int((tm - datetime.datetime.now()).total_seconds())
    if not (seconds > 0):
        print('不是未来时间。')
        return
    os.system('rtcwake -m mem -s {}'.format(seconds))

if __name__ == '__main__':
    main()
