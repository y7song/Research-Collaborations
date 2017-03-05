# Step 5.3.3 This step generates matrix with date and time of the day as two dimensions
#           - The aggregation level for spatial is regions, each containing a set of stations
#           - The aggregation level for time is the calendar date

import datetime

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# list of selected station Numbers
SelStopNo = range(1, 56)

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {2: None, 3: None, 30: None, 12: None}

# selected date range
StartDate = datetime.datetime.strptime("20131001", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131031", "%Y%m%d")

DateDict = {}
CntDict = {}
DeltaDays = (EndDate - StartDate).days
print DeltaDays
for tempdate in range(DeltaDays+1):
    DateDict[tempdate] = None
    CntDict[tempdate] = 0


maxInfo = None
maxHrCnt = 0
while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]

        #if int(inGroupID) not in SelGroup.keys():
        if int(inGroupID) is not None:
            inDate = inYY.zfill(2) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            # print inDate, "->", curweekday

            if StartDate <= curdatetime <= EndDate:
                curDelta = (curdatetime - StartDate).days
                if DateDict[curDelta] is None:
                    DateDict[curDelta] = []
                    for i in range(0, 24):
                        if maxHrCnt < int(inList[i]):
                            maxHrCnt = int(inList[i])
                            maxInfo = rline

                        DateDict[curDelta].append(int(inList[i]))
                    CntDict[curDelta] = 1

                else:
                    curList = DateDict[curDelta]
                    for i in range(0, 24):
                        if maxHrCnt < int(inList[i]):
                            maxHrCnt = int(inList[i])
                            maxInfo = rline
                        curList[i] += int(inList[i])
                    CntDict[curDelta] += 1

    rline = rfile.readline()

rfile.close()
print "Max: ", maxHrCnt
print "---------------------", maxInfo

wfile = open("___PythonAnalysisResults/DT_Results/AggHr_ByDate_AllGrp.txt", "w")

for tempdate in range(DeltaDays+1):

    outlist = DateDict[tempdate]
    outCnt = CntDict[tempdate]
    outdate = StartDate + datetime.timedelta(days=tempdate)
    outstr = outdate.strftime("%Y-%m-%d") + " "
    print outstr, outCnt, ": ",
    for item in outlist:
        print float(item)/outCnt,
        #outstr += str(float(item)/outCnt) + " "
        outstr += str(item) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()