# Step 6.3 Followed by Step 5.3 series for time and date plot
#       - input data format: (WKD: Mon, Tue, Wed, Thu, Fri, Sat, Sun), hr00, hr01, ... hr23, hr24

import numpy as np
import matplotlib.pyplot as plt

# input file path and name
# refer to 5.3.1, 5.3.2, 5.3.3 for reference
intxtfile = "___PythonAnalysisResults_20160319/DT_Results/Average_AllGrp.txt"

# read textfile as numpy array
rfile = open(intxtfile, "r")
npdata = np.loadtxt(rfile, usecols=range(1,25))
#nplabel = np.loadtxt(rfile, usecols=range(0,)).tolist()
nplabel = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print npdata

# create heat map based on the matrix

# for stations with extremely low count, exclude those in visualization and set the color as transparent
masked_array = np.ma.masked_where(npdata < 20.0, npdata)
print masked_array

# plot using color schema Reds and interpolation method nearest
# can be changed to other plotting methods and colors too.
plt.imshow(masked_array, cmap = 'Reds', interpolation='nearest')

# set axis legend as the first column of the text file
y = [0, 1, 2, 3, 4, 5, 6]
plt.yticks(y, nplabel)

# plot matrix
plt.show()









