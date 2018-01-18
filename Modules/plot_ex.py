"""

LIVE PLOTTING
NATHAN NORTH
GE TRANSPORTATION
MARCH 3, 2016

NOTES:
~~

"""

# SECTION 1 - IMPORTS =============================================
from tkinter import *
from plotting import tkplot
import time


# SECTION 2 - INITIALIZATION ======================================
canvasWidth = 1000
canvasHeight = 500

channel = 16
channel2 = 30


# SECTION 3 - FUNCTIONS ===========================================

def DRAreadHeader(line):
    row = line.strip('\n').split('"')
    outrow = row[0].split(' ')
    outrow1 = []
    for item in outrow:
        if item == ' ' or item == '':
            pass
        else:
            outrow1.append(item)

    for item in row:
        if item == ' ' or item == '':
            pass
        else:
            item = item.replace(' ', '')
            outrow1.append(item)
    return outrow1

def DRAreadData(line):
    row = line.strip('\n').split(' ')
    outrow = []
    for item in row:
        if item == ' ' or item == '':
            pass
        else:
            try:
                outrow.append(float(item))
            except:
                outrow.append(item)
    return outrow

def loadData(filename, yindex):
    ydata = []
    with open(filename) as datafile:
        i = 0
        for line in datafile:
            if i == 0:
                header = DRAreadHeader(line)
                i = 1
            else:
                outrow = DRAreadData(line)
                ydata.append(outrow[yindex])
    return header, ydata


xdata = []
header, ydata = loadData('e000003211547.DRA', channel)

for i in range(len(ydata)):
    xdata.append(i)


#Initialize Plots!
myplot = tkplot(xdata, ydata)

myplot.title = header[channel + 1]
myplot.xlabel = 'Time'
myplot.xunit = '[ms]'
myplot.plottype = 'line'
myplot.datacolor = 'red'
myplot.PLOT()
