# Step 0: This module processes raw smart-card data
#   - The original data is provided as text files, each records transactions in a single calendar day
#       >> 2013-10-01 16:13:21 990170470635 102 201333840000009
#       >> yyyy-mm-dd hh:mm:ss xxxxxxxxxxxx(card-id) xxx (group-id) xxxxxxxxxxxxxxx (last three digits for stop-id)

#   - Due to the different format of the raw data, this may not apply to data from other sources

import os.path

# the path of the original dataset
path = "___OriginalCountData_RO/"
dirs = os.listdir(path)

# process one file at a time
for txtfile in dirs:
    print "start ", txtfile
    rfile = open(path + txtfile, "r")
    rline = rfile.readline()
    outList = []

    while rline:
        length = len(rline.split())
        wline = ""
        if length == 6:
            print "----------------combine---------------------", rline
            wline = rline.split()[0:4]
            inStopID = rline.split()[4]+rline.split()[5]
            wline.append(inStopID)
        elif length == 5:
            wline = rline.split()[0:5]
        else:
            # print formats that do not fit the schema and examine its type;
            # mannually or using additional scripts to remove certain types of errors
            # most errors in this dataset is either missing a field OR adding additional space
            print "----------------error?---------------------", rline

        wstring = " ".join(wline)
        # print for test purpose
        # print wstring
        outList.append(wstring)
        rline = rfile.readline()
    
    rfile.close()
    print "---------Finish Reading", txtfile

    # save the cleaned-up data with the same data schema as the original data
    outfilename = "S0_CleanedUpData_RO/" + txtfile
    wfile = open(outfilename, "w")
    wfile.write("\n".join(outList))
    wfile.close()
    print "---------Finished Writing", txtfile




