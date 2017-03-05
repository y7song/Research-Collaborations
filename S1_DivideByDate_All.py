# Step 1: This module processes cleaned-up smart-card data
#   - The original data does not seperate each record as a row
#   - This step may not be necessary due to the different formats of the original data

import os.path

# Open the folder that contains all cleaned up data from Step 0
path = "S0_CleanUpData_RO/"
dirs = os.listdir(path)

dateDict = {}

# process each file a time considering limit in RAM of laptop
# given the data structure, the codes generate one row for each transaction record
for txtfile in dirs:
    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    i = 0
    while rline:
        if len(rline.split()) != 5:
            print "-----------------line", i, " : ", rline
            pass
        else:
            inDate = rline.split()[0]

            if inDate in dateDict:
                dateDict[inDate].append(rline)
            else:
                dateDict[inDate] = [rline]

            inGroup = rline.split()[3]

            # if the group id is not three digits, print the group id
            if len(inGroup) != 3:
                print "---------------------------group id check:", rline
        i += 1
        rline = rfile.readline()

    rfile.close()
    print "Finish reading", txtfile
    print " ---------------------- has a total number of lines:", i

print "Step 1 Finish reading all files"
print "-------------------------------------------------------------------"
print
print


# write the processing outputs into files, each corresponding to one day
for key in dateDict.keys():
    print "Start writing file for Date: ", key, "..."
    print
    inYear, inMonth, inDay = key.split("-")

    outFileName = "S1_DivideByDate/MMDD" + str(inMonth) + str(inDay) + ".txt"
    wfile = open(outFileName, "w")
    curList = dateDict[key]

    j = 0
    for curline in curList:
        wfile.writelines(curline)
        j += 1

    wfile.close()
    # this is an optional step to get a sense of how many transactions are recorded in each day
    print "---------------------- has a total number of lines:", j

print "Step 2 Finished writing all files"




