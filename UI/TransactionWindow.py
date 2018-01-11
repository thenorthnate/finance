import tkinter

def transaction_window(self):
    #Top Level Widgets
    addTransactionWindow = tkinter.Toplevel(self)
    addTransactionWindow.title('Add Transaction')
    addTransactionWindow.geometry('500x500+400+100')
    #.withdraw()
    #.deiconify()
    #.iconify()
    #.state(newstate=None) 'normal', 'iconic', 'withdrawn'
    #.geometry()

    #Middle, Entry Frame
    middleEntryFrame = tkinter.Frame(addTransactionWindow)
    middleEntryFrame.grid(row=0, column=0)
    # Month Selection
    monthSelectionVariable = tkinter.StringVar(addTransactionWindow)
    monthSelectionVariable.set(self.months[self.currentMonth-1])
    monthSelectionMenu = tkinter.OptionMenu(addTransactionWindow, monthSelectionVariable, *self.months)
    monthSelectionMenu.grid(in_=middleEntryFrame, row=0, column=0)
    # Day Entry
    dayEntry = tkinter.Entry(addTransactionWindow, width=2)
    dayEntry.grid(in_=middleEntryFrame, row=0, column=1)
    dayEntryVariable = tkinter.StringVar(addTransactionWindow)
    dayEntryVariable.set(self.currentDay)
    dayEntry["textvariable"] = dayEntryVariable
    dayUpDownFrame = tkinter.Frame(addTransactionWindow)
    dayUpDownFrame.grid(in_=middleEntryFrame, row=0, column=2)
    dayUpButton = tkinter.Button(addTransactionWindow, text='+', command = self.increaseDay)
    dayUpButton.grid(in_=dayUpDownFrame, row=0, column=0)
    dayDownButton = tkinter.Button(addTransactionWindow, text='-', command=self.decreaseDay)
    dayDownButton.grid(in_=dayUpDownFrame, row=1, column=0)
    # Year Entry
    yearEntry = tkinter.Entry(addTransactionWindow, width=4)
    yearEntry.grid(in_=middleEntryFrame, row=0, column=3)
    yearEntryVariable = tkinter.StringVar(addTransactionWindow)
    yearEntryVariable.set(self.currentYear)
    yearEntry["textvariable"] = yearEntryVariable
    yearUpDownFrame = tkinter.Frame(addTransactionWindow)
    yearUpDownFrame.grid(in_=middleEntryFrame, row=0, column=4)
    yearUpButton = tkinter.Button(addTransactionWindow, text='+', command = self.increaseYear)
    yearUpButton.grid(in_=yearUpDownFrame, row=0, column=0)
    yearDownButton = tkinter.Button(addTransactionWindow, text='-', command=self.decreaseYear)
    yearDownButton.grid(in_=yearUpDownFrame, row=1, column=0)
