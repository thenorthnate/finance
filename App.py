#Application class for Cotton application
#Nathan North
#June 27, 2017

from Database import Database
from UI.MainWindow import main_window
from UI.TransactionWindow import transaction_window
from UI.InfoWindow import info_window
from UI.AddUserWindow import add_user_window
import tkinter
import os
import sqlite3
import datetime
import time


class App(tkinter.Frame):
    def __init__(self, master=None):
        #Regular Variables
        self.master = master


        self.userName = 'User'
        self.affirmBoolean = None
        self.cwd = os.getcwd()
        self.filesInCurrentDirectory = os.listdir(self.cwd)
        self.today = datetime.datetime.now()
        self.currentMonth = self.today.month
        self.currentDay = self.today.day
        self.currentYear = self.today.year
        self.months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self.accounts = ('No Accounts Found', )
        self.canvasElements = []
        self.allInfoLabelVariable = 'Account Name: Something Here\nAccount Balance: $100'
        self.affirmationMessage = ''


        #Instantiate Classes
        self.db = Database()

        #UI Variables
        self.canvasWidth = 700
        self.canvasHeight = 600

        #UI Components
        tkinter.Frame.__init__(self, master)
        self.grid(row=0, column=0)
        #master.geometry('1200x630+50+50')
        master.title('Finance Tool')



        menuBar = tkinter.Menu(master)
        master.config(menu=menuBar)
        filemenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.test)
        filemenu.add_command(label="Open...", command=self.test)
        filemenu.add_command(label="Settings", command=self.test)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)

        viewmenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Plot", command=self.test)
        viewmenu.add_command(label="Transactions", command=self.test)

        helpmenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.test)

        main_window(self)

        #Other Initialization Processes
        if 'cotton.db' not in self.filesInCurrentDirectory:
            self.db.createTables()

    def login(self):
        self.addTransactionWindow = tkinter.Toplevel(self)
        self.addTransactionWindow.title('Login')
        self.addTransactionWindow.geometry('500x500+400+100')

    def makeTransactionWindow(self):
        transaction_window(self)

    def searchDatabase(self, event):
        print("The user entered ---->", self.contents.get())
        self.userName = self.contents.get()
        self.contents.set("")

    def launch_info_window(self):
        info_window(self)

    def options(self):
        self.optionsWindow = tkinter.Toplevel(self)
        self.optionsWindow.title('Options')
        self.optionsWindow.geometry('500x500+400+100')

        addUserButton = tkinter.Button(self.optionsWindow, text='Add User', command=self.makeAddUserWindow)
        addUserButton.grid(in_=self.optionsWindow, row=0, column=0)

        addAccountButton = tkinter.Button(self.optionsWindow, text='Add Account', command=self.makeAddAccountWindow)
        addAccountButton.grid(in_=self.optionsWindow, row=1, column=0)

    def makeAddUserWindow(self):
        add_user_window(self)


    def submitUser(self):
        '''
        self.affirmBoolean = False
        self.affirmation()
        while True:
            if self.affirmBoolean:
        '''
        userID = str(int(time.time()))[-2:] + self.firstNameEntryVariable.get()[0:2]
        entry = (userID, self.firstNameEntryVariable.get(), self.lastNameEntryVariable.get(), self.nicknameEntryVariable.get(), self.emailEntryVariable.get(), self.passwordEntryVariable.get(), self.birthdayEntryVariable.get())
        self.db.addUser(entry)
        self.userName = self.nicknameEntryVariable
        self.addUserWindow.withdraw()


    def cancelNewUser(self):
        self.addUserWindow.withdraw()

    def makeAddAccountWindow(self):
        self.optionsWindow.withdraw()
        self.addAccountWindow = tkinter.Toplevel(self)
        self.addAccountWindow.title('Add Account')
        self.addAccountWindow.geometry('500x500+400+100')

    def affirmation(self):
        self.affirmWindow = tkinter.Toplevel(self)
        self.affirmWindow.title('Confirm Entries')
        self.affirmLabel = tkinter.Label(self.affirmWindow, text='Is this Correct?')
        self.affirmLabel.grid(in_=self.affirmWindow, row=0, column=0)
        self.affirmMessageLabel = tkinter.Label(self.affirmWindow, text=self.affirmationMessage)
        self.affirmMessageLabel.grid(in_=self.affirmWindow, row=1, column=0)
        self.affirmYesButton = tkinter.Button(self.affirmWindow, text='Yes', command=self.yesCommand)
        self.affirmYesButton.grid(in_=self.affirmWindow, row=2, column=0)
        self.affirmNoButton = tkinter.Button(self.affirmWindow, text='No', command=self.noCommand)
        self.affirmNoButton.grid(in_=self.affirmWindow, row=3, column=0)

    def yesCommand(self):
        self.affirmBoolean = True
        self.affirmWindow.withdraw()

    def noCommand(self):
        self.affirmBoolean = False
        self.affirmWindow.withdraw()


    def addTransaction(self):
        print("goodbye :(")

    def increaseDay(self):
        currentDayEntry = self.dayEntryVariable.get()
        try:
            currentEntryInt = int(currentDayEntry)
            self.dayEntryVariable.set(str(currentEntryInt+1))
        except ValueError:
            currentEntryInt = self.currentDay
            self.dayEntryVariable.set(str(currentEntryInt))

    def decreaseDay(self):
        currentDayEntry = self.dayEntryVariable.get()
        try:
            currentEntryInt = int(currentDayEntry)
            self.dayEntryVariable.set(str(currentEntryInt-1))
        except ValueError:
            currentEntryInt = self.currentDay
            self.dayEntryVariable.set(str(currentEntryInt))


    def increaseYear(self):
        currentYearEntry = self.yearEntryVariable.get()
        self.yearEntryVariable.set(str(int(currentYearEntry)+1))

    def decreaseYear(self):
        currentYearEntry = self.yearEntryVariable.get()
        self.yearEntryVariable.set(str(int(currentYearEntry)-1))

    def deactivateUIElements(self):
        #This function deactivates all UI components
        #so the user cannot click while an operation is in progress
        self.transactionButton.configure(state=DISABLED)
        self.update()

    def reactivateUIElements(self):
        #This function reactivates all UI elements
        #after an action is completed
        self.transactionButton.configure(state=NORMAL)
        self.update()

    def test(self):
        print('TEST SUCCESS')
