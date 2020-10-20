#AMS129/.../project/python/setup.py
#-------------------------------#
#Joel Aoto                      #
#AMS129, MWF 9:20               #
#project: setup.py              #
#-------------------------------#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#run the fortran programs with the makefile
folder = '../fortran'
cmd1 = 'make'
cmd2 = './main.exe'
os.chdir(folder)
os.system(cmd1)
os.system(cmd2)
os.chdir('../python') #change back to the python directory

fpath8 = os.path.join(folder,"output_8 .txt")
fpath16 = os.path.join(folder,"output_16.txt")
fpath32 = os.path.join(folder,"output_32.txt")
fpath64 = os.path.join(folder,"output_64.txt")

#open the text files creating numpy arrays with the values of the text file
with open(fpath8,'r') as df:
    for line in df:
        data8 = np.loadtxt(df, skiprows = 0)

with open(fpath16,'r') as df1:
    for line in df1:
        data16 = np.loadtxt(df1, skiprows = 0)

with open(fpath32,'r') as df2:
    for line in df2:
        data32 = np.loadtxt(df2, skiprows = 0)

with open(fpath64,'r') as df3:
    for line in df3:
        data64 = np.loadtxt(df3, skiprows = 0)

#functions for calculating the real solution and calculated error
def realsoln(data):
    soln = -np.sqrt(2*np.log(data**2 +1)+4)
    return soln

def solnError(rsol, data):
    error = np.sum(rsol - data)
    return error

#create variables for the different real solutions and calculated error
rsol8 = realsoln(data8[:,0])
rsol16 = realsoln(data16[:,0])
rsol32 = realsoln(data32[:,0])
rsol64 = realsoln(data64[:,0])
error8 = solnError(rsol8, data8[:,1])
error16 = solnError(rsol8, data8[:,1])
error32 = solnError(rsol8, data8[:,1])
error64 = solnError(rsol8, data8[:,1])



#plot the graphs for grid, 8,16,32,64
#with numerical solution and real solution
#with title of the calculated error
plt.figure(figsize = (100,10))
plt.plot(data8[:,0],data8[:,1],color='red', marker='o', linestyle='dashed')
plt.plot(data8[:,0],rsol8,color='blue', linestyle='solid')
plt.xticks(data8[:,0])
plt.xlabel('t-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title(error8)
plt.savefig('result_8.png')
plt.show()

plt.figure(figsize = (100,10))
plt.plot(data16[:,0],data16[:,1],color='red', marker='o', linestyle='dashed' )
plt.plot(data16[:,0],rsol16,color='blue', linestyle='solid')
plt.xticks(data16[:,0])
plt.xlabel('t-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title(error16)
plt.savefig('result_16.png')
plt.show()

plt.figure(figsize = (100,10))
plt.plot(data32[:,0],data32[:,1],color='red', marker='o', linestyle='dashed' )
plt.plot(data32[:,0],rsol32,color='blue', linestyle='solid')
plt.xticks(data32[:,0])
plt.xlabel('t-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title(error32)
plt.savefig('result_32.png')
plt.show()

plt.figure(figsize = (100,10))
plt.plot(data64[:,0],data64[:,1],color='red', marker='o', linestyle='dashed' )
plt.plot(data64[:,0],rsol64,color='blue', linestyle='solid')
plt.xticks(data64[:,0])
plt.xlabel('t-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title(error64)
plt.savefig('result_64.png')
plt.show()

