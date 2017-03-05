# Step 4.2: Unlike step 2.2, this necessary step merges data for all available days into a single txt file


import os.path

# Open a folder
path = "S4_AggregateByHour_RO/"
dirs = os.listdir(path)

wfile = open("SP_MergeAll_RO/AggrHr_All.txt", "w")

for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    while rline:
        wfile.writelines(rline)
        rline = rfile.readline()

    rfile.close()

wfile.close()