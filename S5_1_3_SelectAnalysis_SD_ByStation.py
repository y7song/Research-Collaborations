# Step 5.1.3 This step generates matrix with spatial and date as two dimensions
#           - compared to Step 5.1.1, this step allow visualizing and comparing transaction at individual stations

import datetime

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# Dictionary of selected station Numbers
SelStopNo = range(1, 56)
StopNoDict = {}

StartDate = datetime.datetime.strptime("20131008", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131031", "%Y%m%d")

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {3: None, 30: None}

# select hour of the day
SelHrs = range(0, 24)

# list of selected weekdays
SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for StopNo in SelStopNo:
    StopNoDict[StopNo] = {}
    for weekday in SelWeekday:
        StopNoDict[StopNo][weekday] = 0

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

        if int(inGroupID) in SelGroup.keys():
        #if int(inGroupID) is not None:  # for all group types
            inDate = inYY.zfill(4) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    pass
                    print "Working Saturday"

                if curweekday in SelWeekday:
                    if int(inStopID) in StopNoDict.keys():
                        StopNoDict[int(inStopID)][curweekday] += cumCnt

    rline = rfile.readline()

rfile.close()

wfile = open("___PythonAnalysisResults/SD_Results/AggHrOct_Elder_ByStation_PostHoliday.txt", "w")

for stop in SelStopNo:
    print "hourly count for station:", stop,
    outdict = StopNoDict[stop]
    outstr = str(stop) + " "
    for outkey in SelWeekday:
        print '%7s' % outdict[outkey],
        outstr += str(outdict[outkey]) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()