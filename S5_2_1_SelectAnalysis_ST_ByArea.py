# Step 5.2.2 This step generates matrix with spatial and time of a day as two dimensions
#           - The aggregation level for spatial is region

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

#for key in AreaDict.keys():
#    print key, " :", AreaDict[key]

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# Dictionary of selected station Numbers
SelStopNo = range(1, 56)

StartDate = datetime.datetime.strptime("20131001", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131007", "%Y%m%d")

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {3: None, 30: None, 2: None, 12: None}

# select hour of the day
SelHrs = range(0, 24)

# list of selected weekdays
SelWeekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# initialize AreaCntDict
AreaCntDict = {1: [], 2: [], 3: []}
for area in AreaCntDict.keys():
    AreaCntDict[area] = {}
    for hr in SelHrs:
        AreaCntDict[area][hr] = 0

while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]

        #if int(inGroupID) not in SelGroup.keys():
        if int(inGroupID) is not None:  # for all group types
            inDate = inYY.zfill(4) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    #rline = rflie.readline()
                    #continue
                    print "Working Saturday"

                if curweekday in SelWeekday:
                    for area in AreaDict.keys():
                        if int(inStopID) in AreaDict[area]:
                            for hr in SelHrs:
                                AreaCntDict[area][hr] += int(inList[hr])

    rline = rfile.readline()

rfile.close()

wfile = open("___PythonAnalysisResults/ST_Results/AggHr_AllGrp_ByArea_Holiday.txt", "w")

for area in AreaCntDict:
    print "hourly count for area:", area,
    outdict = AreaCntDict[area]
    outstr = str(area) + " "
    for hr in SelHrs:
        print '%7s' % outdict[hr],
        outstr += str(outdict[hr]) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()