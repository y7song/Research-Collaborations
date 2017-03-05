# Step 6.2 Followed by Step 5.2 series for station and time plot
#       - input data format: (Station/Region: ###), hr00, hr01, ... hr23, hr24

import numpy as np
import matplotlib.pyplot as plt

# input file path and name
# refer to 5.3.1, 5.3.2, 5.3.3 for reference
intxtfile = "___PythonAnalysisResults_20160319/ST_Results/Average_AllGrp_ByStation_PostHoliday.txt"

# read textfile as numpy array
rfile = open(intxtfile, "r")
npdata = np.loadtxt(rfile, usecols=range(1,24))
nplabel = np.loadtxt(rfile, usecols=range(0,)).tolist()
# print npdata
print nplabel

# create heat map based on the matrix

# for stations with extremely low count, exclude those in visualization and set the color as transparent
masked_array = np.ma.masked_where(npdata < 20.0, npdata)
#print masked_array

# plot using color schema Reds and interpolation method nearest
# can be changed to other plotting methods and colors too.
plt.imshow(masked_array, cmap = 'Reds', interpolation='nearest')

# set axis legend as the first column of the text file
y = range(0, len(nplabel))
plt.yticks(y, nplabel)

# plot matrix
plt.show()









