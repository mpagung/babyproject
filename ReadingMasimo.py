import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# with open('testwithartifact') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     timerec=[]
#     signal1=[]
#     signal2=[]
#     for row in csv_reader:
#         timerec.append(row[0])
#         signal1.append(row[3])
#         signal2.append(row[5])

dataread=pd.read_csv("testnonin")
print(dataread)
plt.figure()
dataread.plot()
#times=date2num(timerec)
#print(timerec)
#plt.plot(timerec,signal1)
#plt.show()
