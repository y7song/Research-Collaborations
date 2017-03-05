# Step 2.1 Sort the records for each cardID by its recorded time hh:mm:ss (ascending), and add sequence number
#   - Although we will not use this sorting result to analyze individuals' travel patterns,
#   - it would be still useful to add a sequence number in preparation for later analysis

from operator import itemgetter
import os.path
import string

# Open a folder
path = "S1_DivideByDate_RO/"
dirs = os.listdir(path)

for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()
    CardIDDict = {}

    while rline:
        i = len(rline.split())
        if i != 5:
            print "-----------------line", i, " : ", rline
            pass
        else:
            inDate, inTime, inCardID, inGroupID, inStopID = rline.split()

            if inCardID in CardIDDict:
                CardIDDict[inCardID].append([inDate, inCardID, inTime, inGroupID, inStopID, "None"])
            else:
                CardIDDict[inCardID] = [[inDate, inCardID, inTime, inGroupID, inStopID, "None"]]

        rline = rfile.readline()

    rfile.close()
    print "Finish reading", txtfile, "..."

    OutList = []
    for key, curList in CardIDDict.items():
        # print is for testing purpose
        # print key
        # print curList
        # print "sort=>",

        # the index for "time" in the dictionary CardIDDict for the item with key inCardID
        # sort the records for current inCardID ascending
        curList.sort(key=itemgetter(2))

        # print curList
        # print
        # print

        # add squence number after sorting
        i = 1
        for record in curList:
            record[5] = str(i)
            curstr = " ".join(record)
            OutList.append(curstr)
            OutList.append("\n")
            i += 1
        # print curList

    # write the sorting results to new files with similar naming system
    outfile = string.replace(txtfile, "MMDD", "AddSeq")
    wfile = open("S2_SortCard_AddSeq/" + outfile, "w")

    for curLine in OutList:
        wfile.writelines(curLine)

    wfile.close()
    print "---------- Finish writing", outfile, "..."

print "Finish All"