# Step 5.3.1 This step generates matrix with day of the week and time of a day as two dimensions
#           - The aggregation level for spatial is individual station, which is the lowest level
#           - The aggregation level for time is the day of the week 

import datetime

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

WeekdayDict = {"Mon": None, "Tue": None, "Wed": None, "Thu": None, "Fri": None, "Sat": None, "Sun": None}

# list of selected station Numbers
SelStopNo = range(1, 56)

# list of selected groups
# 101: anonymous, 102: anonymous, 002: student(half-price), 003: 70+ elder (free), 030: 60+ elder (half-price), other:
# SelGroup = {101: None, 102: None, 2: None, 3: None, 30: None, 12: None}
SelGroup = {2: None, 3: None, 30: None, 12: None}

# selected date range
StartDate = datetime.datetime.strptime("20131001", "%Y%m%d")
EndDate = datetime.datetime.strptime("20131007", "%Y%m%d")


while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        inList = rline.split()[5:29]

        if int(inGroupID) not in SelGroup.keys():
        #if int(inGroupID) is not None:
            inDate = inYY.zfill(2) + inMM.zfill(2) + inDD.zfill(2)
            curdatetime = datetime.datetime.strptime(inDate, '%Y%m%d')
            curweekday = curdatetime.strftime('%a')
            # print inDate, "->", curweekday

            if StartDate <= curdatetime <= EndDate:
                # working on Sat after holiday
                if curdatetime == datetime.datetime.strptime("20131012", "%Y%m%d"):
                    rline = rfile.readline()
                    continue
                    #print "Working Saturday"

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

wfile = open("___PythonAnalysisResults/DT_Results/AggHr_Other_Holiday.txt", "w")

for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    print "hourly count for weekday:", weekday,
    outlist = WeekdayDict[weekday]
    outstr = weekday + " "
    for item in outlist:
        print item,
        outstr += str(item) + " "
    outstr += "\n"
    print

    wfile.writelines(outstr)

wfile.close()