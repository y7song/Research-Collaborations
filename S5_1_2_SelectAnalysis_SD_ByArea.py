# Step 5.1.2 This step generates matrix with spatial and date as two dimensions
#           - compared to Step 5.1.1, this step allow further aggregating stations into regions

import datetime

# station type: 1= urban, 2= suburban, 3=exurban
AreaDict = {1: [], 2: [], 3: []}

locfile = open("J:/Research/Collaborations/2016_UMN_YinglingFan_TrafficCubeChina/MATLABCodes_v1/"
               "___SpatialAnalysisResults/StationLocTypeTxt_Sel.txt", "r")
locline = locfile.readline()

while locline:
    inID, inLine, inArea = locline.split()
    AreaDict[int(inArea)].append(int(inID))
    locline = locfile.readline()

locfile.close()

# in case that there are other region definition, this provides an option to deal with this situation
# for key in AreaDict.keys():
#    print key, " :", AreaDict[key]

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

StartDate = datetime.datetime.strptime("20131001", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131031", "%Y%m%d")

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {12: None, 2: None, 3: None, 30: None}

# select hour of the day
SelHrs = range(0, 24)

# list of selected weekdays
SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

AreaCntDict = {1: {}, 2: {}, 3: {}}
for weekday in SelWeekday:
    for key in AreaCntDict.keys():
        AreaCntDict[key][weekday] = 0

#print "------------- Initial Dictionary ---------------"
#print AreaCntDict

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

        if int(inGroupID) not in SelGroup.keys():
        #if int(inGroupID) is not None:  # for all group types
            inDate = inYY.zfill(4) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    #pass
                    print "Working Saturday"

                if curweekday in SelWeekday:
                    for area in AreaCntDict.keys():
                        if int(inStopID) in AreaDict[area]:
                            AreaCntDict[area][curweekday] += cumCnt

    rline = rfile.readline()

rfile.close()


wfile = open("___PythonAnalysisResults/SD_Results/AggHrOct_OthersV2_ByArea.txt", "w")

for area in AreaCntDict.keys():
    print "hourly count for area:", area,
    outdict = AreaCntDict[area]
    outstr = str(area) + " "
    for outkey in SelWeekday:
        print '%7s' % outdict[outkey],
        outstr += str(outdict[outkey]) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()