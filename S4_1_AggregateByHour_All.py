# Step 4.1 For the analysis of our paper, the finest unit for dimension T is hour
#           - It is also possible to create finer scale for analysis.
#           - To do it, use the field inmm to create 5, 10, 15, 30, ... minutes as time intervals

import os.path
import string

# Open the folder contains the selected and sorted results
path = "S3_StopIDGroupIDSort_RO/"
dirs = os.listdir(path)

# process one file at a time
for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    StationDict = {}

    while rline:
        i = len(rline.split())
        if i != 4:
            print "-----------------line", i, " : ", rline
            pass
        else:
            inStopID, inGroupID, inDate, inTime = rline.split()
            inStopNo = int(inStopID)
            inGroupNo = int(inGroupID)
            inYY, inMM, inDD = int(inDate[0:4]), int(inDate[5:7]), int(inDate[8:10])
            inhh, inmm, inss = int(inTime[0:2]), int(inTime[3:5]), int(inTime[6:8])

            if inStopNo in StationDict.keys():
                curDict = StationDict[inStopNo]
                # if the current stop has already added in the dictionary, add the current record to its dictionary
                if inGroupNo in curDict.keys():
                    curIndex = inhh + 5
                    curDict[inGroupNo][curIndex] += 1

                # if the current stop has not been added into the dictionary, initialize the dictionary for that stop
                else:
                    StationDict[inStopNo][inGroupNo] = [inStopNo, inGroupNo, inYY, inMM, inDD]
                    for hr in range(0, 24):
                        StationDict[inStopNo][inGroupNo].append(0)

            else:
                StationDict[inStopNo] = {}
                StationDict[inStopNo][inGroupNo] = [inStopNo, inGroupNo, inYY, inMM, inDD]

                for hr in range(0, 24):
                    StationDict[inStopNo][inGroupNo].append(0)
                    #index for hour 0, 1, 2, ..., 23 from 5, 6, 7, 8, ...., 28

        rline = rfile.readline()

    rfile.close()
    print "--------------- Finish reading file: ", txtfile

    outfile = string.replace(txtfile, "StGrp", "AggHr")
    wfile = open("S4_AggregateByHour/" + outfile, "w")

    for key, item in StationDict.items():
        #key refers to the station id
        #item is a dictionary of user groups with recorded transactions

        for key2, item2 in item.items():
            # key 2 is the user group id
            outStr = ""
            for item3 in item2:
                # item2 is the list of recorded 24 hours of transaction counts
                outStr = outStr + str(item3) + " "
            outStr += "\n"
            wfile.writelines(outStr)

    wfile.close()
    print "---------------_____ Finish writing file: ", outfile