# Step 3.2: Similar to step 2.2, this optional step merges data for all available days into a single txt file
import os.path


path = "S3_StopIDGroupIDSort_RO/"
dirs = os.listdir(path)

wfile = open("SP_MergeAll_RO/StGrp_All.txt", "w")

for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    while rline:
        wfile.writelines(rline)
        rline = rfile.readline()

    rfile.close()

wfile.close()