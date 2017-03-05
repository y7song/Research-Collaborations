# Step 4.3: After getting sum of all counts, this step calculate the average hourly counts
#           - this is the last step for pre-prossing the data
#           - the merge text file is the original data cube created for visualisation
#           - the later steps will use the merged text file

rfile = open("SP_MergeAll_RO/AggrHr_All.txt", "r")
rline = rfile.readline()

# list of selected groups
# 0(101 & 102: anonymous, others), 1(002: student), 2(003: 70+ elder, 030: 60+ elder), 3(012:Disable)
GroupList = [{},{},{},{}]

while rline:
    i = len(rline.split())
    if i != 29:
        print "-----------------line", i, " : ", rline
        pass
    else:
        inStopID, inGroupID, inYY, inMM, inDD = rline.split()[0:5]
        curDate = int(inYY) * 10000 + int(inMM) * 100 + int(inDD)

        curIndex = None
        if inGroupID == "2":
            curIndex = 1
        elif inGroupID == "3" or inGroupID == "30":
            curIndex = 2
        elif inGroupID == "12":
            curIndex = 3
        else:
            curIndex = 0

        if curIndex is None:
            print "group not found!", inGroupID
            pass
        else:
            curCntList = rline.split()[5:29]
            sum = 0
            for item in curCntList:
                sum += int(item)

            if curDate in GroupList[curIndex].keys():
                GroupList[curIndex][curDate] += sum  # store the total transaction counts for that date & group
            else:
                GroupList[curIndex][curDate] = sum

    rline = rfile.readline()

print "Finish Reading"

outGroupList = []
for i in range(0,4):
    curGroupDict = GroupList[i]
    sum = 0
    cnt = 0
    sum1 = 0
    cnt1 = 0
    sum2 = 0
    cnt2 = 0
    for key, item in curGroupDict.items():
        sum += curGroupDict[key]
        cnt += 1
        keydate = key % 100
        if keydate <= 7 or keydate == 12:
            sum1 += curGroupDict[key]
            cnt1 += 1
        else:
            sum2 += curGroupDict[key]
            cnt2 += 1
    average = float(sum)/cnt
    average1 = float(sum1)/cnt1
    average2 = float(sum2)/cnt2
    print i, ",", average, average1, average2



