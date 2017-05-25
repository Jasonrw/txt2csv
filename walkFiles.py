# -*- coding: utf-8 -*-
import os
from time import clock
list_dirs = os.walk("/media/jason/Seagate Backup Plus Drive/Learning/Dic")
count =0
interval = 1000000
tempCount = 0
start = clock()
for root, dirs, files in list_dirs:
    #for d in dirs:
    #    print os.path.join(root, d)
    for f in files:
        #print os.path.join(root, f)
        external = os.path.splitext(f)[1]
        if external == ".txt" or external == ".csv" or external == ".sql":
            with open(os.path.join(root, f), "r") as fi:
                while True:
                    lines = fi.readlines(100000)
                    if not lines:
                        break
                    for line in lines:
                        count = count + 1
                        tempCount = tempCount + 1
                        print count
                        end = clock()
                        if (end - start)>interval:
                            print "Total:"
                            print count
                            print "speed:"
                            print tempCount
                            tempCount = 0
                            interval += 1000000
