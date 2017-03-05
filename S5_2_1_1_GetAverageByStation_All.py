# Step 5.2.1.1 This step is a followed up step after creating cube with dimension station and time
#       - the average counts for selected stations only

import os.path

path = "___PythonAnalysisResults/ST_Results/"
dirs = os.listdir(path)

for txtfile in dirs:
    if txtfile[0:5] != "AggHr":
        print txtfile[0:5]
        continue

    # Number of Weekdays from Monday to Sunday
    if txtfile[-12:] == "_Holiday.txt":
        DateCnt = 7.0
    elif txtfile[-16:] == "_PostHoliday.txt":
        DateCnt = 24.0
    else:
        DateCnt = 31.0

    StationCntDict = {"1": 11, "2": 39, "3": 5}

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    wfile = open(path + txtfile.replace("AggHr", "Average"), "w")
    print "------------------------------", txtfile, "-------------------------"

    while rline:

        if len(rline.split()) != 25:
            print "-----------------: ", rline
            pass
        else:
            inList = rline.split()[1:]

            outStr = rline.split()[0]
            outCnt = StationCntDict[outStr]*DateCnt

            for item in inList:
                outStr += " " + str(float(item)/outCnt)

        outStr += "\n"
        print outStr

        wfile.writelines(outStr)

        rline = rfile.readline()



    rfile.close()
    wfile.close()

