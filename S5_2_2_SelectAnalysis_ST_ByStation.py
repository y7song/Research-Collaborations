# Step 5.2.1 This step generates matrix with spatial and time of a day as two dimensions
#           - The aggregation level for spatial is individual station, which is the lowest level
import datetime

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# Dictionary of selected station Numbers
#SelStopNo = range(1, 56)
SelStopNo = [6, 7, 8, 9, 10, 11, 12, 13, 24, 25, 26, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 39, 40, 53, 54, 55]
StopNoDict = {}

StartDate = datetime.datetime.strptime("20131002", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131002", "%Y%m%d")

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {12: None}

# select hour of the day
SelHrs = range(0, 24)

# list of selected weekdays
SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri"]

for StopNo in SelStopNo:
    StopNoDict[StopNo] = {}
    for hr in SelHrs:
        StopNoDict[StopNo][hr] = 0

while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]

        #if int(inGroupID) in SelGroup.keys():
        if int(inGroupID) is not None:  # for all group types
            inDate = inYY.zfill(4) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    # continue
                    print "Working Saturday"
                    if int(inStopID) in StopNoDict.keys():
                        for hr in SelHrs:
                            StopNoDict[int(inStopID)][hr] += int(inList[hr])

                if curweekday in SelWeekday:
                    if int(inStopID) in StopNoDict.keys():
                        for hr in SelHrs:
                            StopNoDict[int(inStopID)][hr] += int(inList[hr])

    rline = rfile.readline()

rfile.close()

wfile = open("___PythonAnalysisResults/ST_Results/AggHr_AllGrp_ByStation_2ndHoliday.txt", "w")

for stop in SelStopNo:
    print "hourly count for station:", stop,
    outdict = StopNoDict[stop]
    outstr = str(stop) + " "
    for hr in SelHrs:
        print '%7s' % outdict[hr],
        outstr += str(outdict[hr]) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()