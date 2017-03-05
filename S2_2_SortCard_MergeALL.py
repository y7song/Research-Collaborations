# Step 2.2: This optional step merges data for all available days into a single txt file
import os.path


# Open the folder for files with ordered records
path = "S2_SortCard_AddSeq_Extra/"
dirs = os.listdir(path)

wfile = open("SP_MergeAll_RO/AddSeq_MergeAll.txt", "w")

for txtfile in dirs:
    print "start ", txtfile

    rfile = open(path + txtfile, "r")
    rline = rfile.readline()

    while rline:
        wfile.writelines(rline)
        rline = rfile.readline()

    rfile.close()
    print "Finish reading file", txtfile

wfile.close()
print "--------------- Finish writing ---------"