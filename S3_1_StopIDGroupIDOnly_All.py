# Step 3.1 Since the analysis will focus on the aggregation level of Card Group for the user (social) dimension
#           we will not use the field inCardID. This steps delete the field inCardID.

from operator import itemgetter
import os.path
import string

# Open the folder for data by MMDD
path = "S1_DivideByDate_RO/"
dirs = os.listdir(path)

for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    StationDict = {}

    while rline:
        i = len(rline.split())
        if i != 5:
            print "-----------------line", i, " : ", rline
            pass
        else:
            inDate, inTime, inCardID, inGroupID, inStopID = rline.split()
            StationID = inStopID[-5:]
            # print StationID

            # select and re-order the original recrods
            if StationID in StationDict.keys():
                StationDict[StationID].append([StationID, inGroupID, inDate, inTime])
            else:
                StationDict[StationID] = [[StationID, inGroupID, inDate, inTime]]

        rline = rfile.readline()

    rfile.close()
    print "---------------finish reading ", txtfile

    OutList = []

    for key, curList in StationDict.items():
        #print key
        #print curList
        #print "sort=>",

        # sort the original record for each station for each date ascending
        # in fact, each individual file only contains data for one day
        # the scripts include the second field for sorting, just in case other data have all dates in one file
        curList.sort(key=itemgetter(1, 3))


        #print curList
        #print
        #print

        for record in curList:
            OutList.append(" ".join(record))
            OutList.append("\n")


    # write the selected and sorted results into individual files
    outfile = string.replace(txtfile, "MMDD", "StGrp")
    wfile = open("S3_StopIDGroupIDSort/" + outfile, "w")

    for curLine in OutList:
        wfile.writelines(curLine)

    wfile.close()
    print "--------------------------------finish writing ", outfile

print "Finish writing all"