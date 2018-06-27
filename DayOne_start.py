#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#
# DayOne_start : Open latest Day One 
#
#

import os
import glob
import subprocess

def main():
    
    print('* DayOne_start')

    files = []
    files = glob.glob('/Applications/Day One*')

    dayOne_latest = ""

    cTime = 0
    cTime_latest = 0

    i = 0
    for dayOne in files:
        print(dayOne + " : " + str(os.path.getctime(dayOne)))
        
        if i == 0:
            dayOne_latest = dayOne
            cTime_latest = os.path.getctime(dayOne)
        else: pass

        i += 1

        cTime = os.path.getctime(dayOne)

        if cTime > cTime_latest:
            cTime_latest = cTime
            dayOne_latest = dayOne
        else: pass

    print('open [' + dayOne_latest + ']')

    res = subprocess.call(["open","-a",dayOne_latest])

if __name__ == '__main__':
    main()
