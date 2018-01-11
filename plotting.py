'''
NATHAN NORTH
GE TRANSPORTATION
Plotting Library using tkinter
'''

from tkinter import *

class tkplot:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        self.datacolor = 'black'
        self.drawingArea = 'default'
        self.canvasWidth = 800
        self.canvasHeight = 400
        self.borderWidth = 100
        self.plottype = 'scatter'
        self.dash = None #(4,4)
        self.forceScale = False
        self.multiplot = True
        #Metadata
        self.showdata = True
        self.title = ''
        self.xlabel = ''
        self.ylabel = ''
        self.xunit = ''
        self.yunit = ''


    def help(self):
        print('plot - Class Parameters:')
        print('xlabel, ylabel, xunit, yunit, ydata, xdata, drawingArea, forceScale')


    def showMeta(self, drawHeight, drawWidth, sdy, sdx, maxY, minY, yMove, yScale, maxX, minX, xMove, xScale):
        #Title and Labels
        self.drawingArea.create_text(self.canvasWidth/2, sdy/2, text=self.title, font=('Times New Roman', 16))
        self.drawingArea.create_text(self.canvasWidth/2, self.canvasHeight-sdy/8, text=self.xlabel + ' ' + self.xunit)

        #Y Axis Data
        self.drawingArea.create_line(sdx, sdy/2, sdx, self.canvasHeight-3*sdy/4)
        aveVal = round((maxY+minY)/2, 2)
        newV = drawHeight - ((aveVal + yMove) * yScale) + sdy
        self.drawingArea.create_line(sdx, newV, sdx+1*sdx/7, newV)
        self.drawingArea.create_text(sdx/2, newV, text=str(aveVal))
        maxVal = round(maxY, 2)
        newV = drawHeight - ((maxVal + yMove) * yScale) + sdy
        self.drawingArea.create_line(sdx, newV, sdx+1*sdx/7, newV)
        self.drawingArea.create_text(sdx/2, newV, text=str(maxVal))
        minVal = round(minY, 2)
        newV = drawHeight - ((minVal + yMove) * yScale) + sdy
        self.drawingArea.create_line(sdx, newV, sdx+1*sdx/7, newV)
        self.drawingArea.create_text(sdx/2, newV, text=str(minVal))

        #X Axis Data
        self.drawingArea.create_line(sdx, self.canvasHeight-3*sdy/4, self.canvasWidth-sdx/2, self.canvasHeight-3*sdy/4)
        aveVal = round((maxX+minX)/2, 2)
        newV = ((aveVal + xMove) * xScale) + sdx
        self.drawingArea.create_line(newV, self.canvasHeight-3*sdy/4-sdy/7, newV, self.canvasHeight-3*sdy/4)
        self.drawingArea.create_text(newV, self.canvasHeight-sdy/2, text=str(aveVal))

        Val = round(maxX, 2)
        newV = ((Val + xMove) * xScale) + sdx
        self.drawingArea.create_line(newV, self.canvasHeight-3*sdy/4-sdy/7, newV, self.canvasHeight-3*sdy/4)
        self.drawingArea.create_text(newV, self.canvasHeight-sdy/2, text=str(Val))

        Val = round(minX, 2)
        newV = ((Val + xMove) * xScale) + sdx
        self.drawingArea.create_line(newV, self.canvasHeight-3*sdy/4-sdy/7, newV, self.canvasHeight-3*sdy/4)
        self.drawingArea.create_text(newV, self.canvasHeight-sdy/2, text=str(Val))


    def PLOT(self):
        root = Tk()
        root.geometry('1200x630+20+20')
        root.title('Plot')
        self.drawingArea = Canvas(root, width=self.canvasWidth, height=self.canvasHeight, background='white')
        self.drawingArea.delete(ALL)
        #Initialization of parameters
        drawWidth = self.canvasWidth - self.borderWidth
        drawHeight = self.canvasHeight - self.borderWidth
        sdy = self.borderWidth/2
        sdx = self.borderWidth/2

        #Find maximum scaling of data points
        maxY = max(self.ydata)
        minY = min(self.ydata)
        maxX = max(self.xdata)
        minX = min(self.xdata)

        yMove = 0-minY
        yDiff = maxY-minY
        xMove = 0-minX
        xDiff = maxX-minX

        try:
            #Try to determine the local scaling of the plot
            yScale = drawHeight/yDiff
            xScale = drawWidth/xDiff
        except ZeroDivisionError:
            #If there is only one point... scale should be 1
            yScale = 1
            xScale = 1

        if self.forceScale:
            if self.multiplot:
                #If forced scaling isn't 0, reset the following variables
                yDiff = self.ymaxofalldata-self.yminofalldata
                try:
                    self.yforceScale = drawHeight/yDiff
                except ZeroDivisionError:
                    self.yforceScale = 1
                yScale = self.yforceScale
                yMove = 0 - self.yminofalldata
                maxY = self.ymaxofalldata
                minY = self.yminofalldata

                #Forced Scaling of x data is turned on
                xDiff = self.xmaxofalldata - self.xminofalldata
                try:
                    self.xforceScale = drawWidth/xDiff
                except ZeroDivisionError:
                    self.xforceScale = 1
                xScale = self.xforceScale
                xMove = 0 - self.xminofalldata
            else:
                #If you want to zoom on the data
                #Should work to scale all data the same way...
                pass

        if self.plottype == 'scatter':
            i = 0
            for point in self.ydata:
                newY = drawHeight - ((point + yMove) * yScale) + sdy
                newX = ((self.xdata[i] + xMove)*xScale) + sdx
                self.drawingArea.create_text(newX, newY, text='*', fill=self.datacolor)
                i += 1
            if self.showdata:
                self.showMeta(drawHeight, drawWidth, sdy, sdx, maxY, minY, yMove, yScale, maxX, minX, xMove, xScale)

        elif self.plottype == 'line':
            for i in range(len(self.ydata)-1):
                newY1 = drawHeight - ((self.ydata[i] + yMove) * yScale) + sdy
                newY2 = drawHeight - ((self.ydata[i+1] + yMove) * yScale) + sdy
                newX1 = ((self.xdata[i] + xMove) * xScale) + sdx
                newX2 = ((self.xdata[i+1] + xMove) * xScale) + sdx
                self.drawingArea.create_line(newX1, newY1, newX2, newY2, fill=self.datacolor, dash=self.dash)
            if self.showdata:
                self.showMeta(drawHeight, drawWidth, sdy, sdx, maxY, minY, yMove, yScale, maxX, minX, xMove, xScale)

        self.drawingArea.grid(row=0, column=0)
        root.mainloop()
