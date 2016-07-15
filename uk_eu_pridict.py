import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import csv

argvs = sys.argv
if (len(argvs) != 2):
	print('Usage: $ python %s filename' % argvs[0])
	exit()
 
csvfile = argvs[1]
try:
        f = open(csvfile,"r")
        dates = list(csv.reader(f))
except:
	print('faild to load %s' % csvfile)
	exit()


# date = np.array([])
date = []
LeaveEU = []
RemainEU = []
Undicided = []
for row in dates:
    # row[0] = row[1]
    # print(row[0])
    # np.append(date,row[0])
    date.append(row[0])
    LeaveEU.append(row[1])
    RemainEU.append(row[2])
    Undicided.append(row[3])

del date[0]
del LeaveEU[0]
del RemainEU[0]
del Undicided[0]

date = np.array(date)
LeaveEU = np.array(LeaveEU)
RemainEU = np.array(RemainEU)
Undicided = np.array(Undicided)
print(date,LeaveEU,RemainEU,Undicided)
f.close()

plt.plot(date,LeaveEU)
plt.plot(date,RemainEU)
plt.plot(date,Undicided)
plt.show()
