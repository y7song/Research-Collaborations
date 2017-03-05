# Step 5.1.1 This step generates matrix with spatial and date as two dimensions

import datetime

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# Dictionary of selected station Numbers
SelStopNo = range(1, 56)
StopNoDict = {}

# Select the range of date of interest in format of YYYYmmDD
StartDate = datetime.datetime.strptime("20131001", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131031", "%Y%m%d")
deltaDate = EndDate - StartDate

for StopNo in SelStopNo:
    StopNoDict[StopNo] = []
    for i in range(deltaDate.days + 1):
        # print StartDate + datetime.timedelta(days = i)
        StopNoDict[int(StopNo)].append(0)

# list of selected weekdays
# can limited to weekday or weekend based on interests
SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price),
# 012: disabled, other:

# can modified according to interested user group
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {2: None, 3: None, 30: None, 12: None}

# select hour of the day
SelHrs = range(0, 24)

while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]
        cumCnt = 0
        for hr in SelHrs:
            cumCnt += int(inList[hr])
        # print "current total count", cumCnt, "---------------"
        if int(inGroupID) not in SelGroup.keys():
            # if int(inGroupID) is not None: #for all group types
            inDate = inYY.zfill(4) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')
            curdeltadate = curdatetime - StartDate
            curindex = curdeltadate.days

            if StartDate <= curdatetime <= EndDate:
                if curweekday in SelWeekday:
                    if int(inStopID) in StopNoDict.keys():
                        StopNoDict[int(inStopID)][curindex] += cumCnt

    rline = rfile.readline()

rfile.close()

wfile = open("___PythonAnalysisResults/SD_Results/AggHrOct_OthersV2.txt", "w")

for stop in SelStopNo:
    print "hourly count for station:", stop,
    outlist = StopNoDict[stop]
    outstr = str(stop) + " "
    for item in outlist:
        print '%7s' % item,
        outstr += str(item) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()