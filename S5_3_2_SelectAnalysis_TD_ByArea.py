# Step 5.3.2 This step generates matrix with day of the week and time of a day as two dimensions
#           - The aggregation level for spatial is regions, each containing a set of stations
#           - The aggregation level for time is the day of the week

import datetime

# ----------------------------------------------- seperate by different area -----------------------------
# select station type: 1= urban, 2= suburban, 3=exurban
seltype = 1
stationIDList = []

locfile = open("J:/Research/Collaborations/2016_UMN_YinglingFan_TrafficCubeChina/MATLABCodes_v1"
               "/___SpatialAnalysisResults/StationLocTypeTxt_Sel.txt", "r")
locline = locfile.readline()

while locline:
    inID, inLine, inArea = locline.split()
    if int(inArea) == seltype and int(inID) not in stationIDList:
        stationIDList.append(int(inID))
    locline = locfile.readline()

locfile.close()
print "selected station IDs: ", stationIDList
stationCnt = len(stationIDList)
print stationCnt

# ----------------------------------------------- start analysis data -----------------------------
rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

WeekdayDict = {"Mon": None, "Tue": None, "Wed": None, "Thu": None, "Fri": None, "Sat": None, "Sun": None}

# list of selected station Numbers
SelStopNo = range(1, 56)

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {2: None, 3: None, 30: None}

# selected date range
StartDate = datetime.datetime.strptime("20131008", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131031", "%Y%m%d")


while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]

        # if int(inGroupID) not in SelGroup.keys() and int(inStopID) in stationIDList:
        if int(inGroupID) is not None and int(inStopID) in stationIDList:
            inDate = inYY.zfill(2) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')
            # print inDate, "->", curweekday

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    rline = rfile.readline()
                    continue
                    print "Working Saturday"

                if WeekdayDict[curweekday] is None:
                    WeekdayDict[curweekday] = []
                    for i in range(0, 24):
                        WeekdayDict[curweekday].append(int(inList[i]))

                else:
                    curList = WeekdayDict[curweekday]
                    for i in range(0, 24):
                        curList[i] += int(inList[i])

    rline = rfile.readline()

rfile.close()

wfile = open("___PythonAnalysisResults/DT_Results/AggHr_AllGrp_Urban_PostHoliday_v2.txt", "w")

for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    print weekday,
    outlist = WeekdayDict[weekday]
    outstr = weekday + " "
    for item in outlist:
        outstr += str(float(item)/stationCnt) + " "
        print '%7s' % str(float(item)/stationCnt),
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()