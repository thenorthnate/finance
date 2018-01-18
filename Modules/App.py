#Application class for Cotton application
#Nathan North
#June 27, 2017

'''
with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
'''

from Modules.Main import main_window
from Modules.ViewTransactions import ViewTransactions
from Modules.AddTransaction import AddTransaction
from Modules.InfoWindow import info_window
from Modules.AddUser import AddUser
from Modules.Login import Login

from Modules.Database import Database

import tkinter
import os
import sqlite3
import datetime
import time
import json

# NOTE: Make the main window have nothing on it, and disappear - this way you have to quit, or exit
# before the program will exit...

class App(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid(row=0, column=0)

        self.make_menu()
        self.master = master

        self.cwd = os.getcwd()
        self.filesInCurrentDirectory = os.listdir(self.cwd)
        self.config = {}
        self.read_config()

        # Instantiations
        self.loginWindow = Login(self)
        self.transactionWindow = ViewTransactions(self)
        self.db = Database()
        self.main_window(self)

        self.username = ''
        self.password = ''
        self.loggedIn = False

        self.accounts = ('No Accounts Found', )
        self.master.state('withdrawn')

        #Other Initialization Processes
        if 'cotton.db' not in self.filesInCurrentDirectory:
            self.db.createTables()



    def read_config(self):
        configPath = self.cwd + '/Static/Settings/config.json'
        with open(configPath, 'r') as inputFile:
            self.config = json.load(inputFile)


    def make_menu(self):
        menuBar = tkinter.Menu(self.master)
        self.master.config(menu=menuBar)
        filemenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="About", command=self.test)
        filemenu.add_command(label="Settings", command=self.test)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

        viewmenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Controls", command=self.test)
        viewmenu.add_command(label="Transactions", command=self.makeTransactionWindow)
        viewmenu.add_command(label="Info", command=self.test)

        accountmenu = tkinter.Menu(menuBar)
        menuBar.add_cascade(label="Account", menu=accountmenu)
        accountmenu.add_command(label="Add User", command=self.options)
        accountmenu.add_command(label="Add Account", command=self.test)


    def main_window(self, event):
        self.master.title(self.config['main']['title'])
        canvasWidth = self.config['main']['component']['canvas']['width']
        canvasHeight = self.config['main']['component']['canvas']['height']
        geo = str(canvasWidth) + 'x' + str(canvasHeight) + '+10+30'
        self.master.geometry(geo)
        topFrame = tkinter.Frame(self)
        topFrame.grid(row=0, column=0)
        self.canvas = tkinter.Canvas(self, width=canvasWidth, height=canvasHeight)
        self.canvas.grid(in_=topFrame, row=0, column=0)
        self.master.bind('<Button-1>', self.canvas_interaction)

        half = self.config['main']['component']['canvas']['height']/2
        xa = 50
        ya = half/2
        xb = half+50
        yb = half + ya
        # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_arc.html
        self.canvas.create_arc(xa, ya, xb, yb, fill="#0776A0", outline="#FF8500", style=tkinter.PIESLICE, start=60, extent=180)
        self.canvas.create_arc(xa, ya, xb, yb, fill="#FF8500", outline="#0776A0", style=tkinter.PIESLICE, start=240, extent=180)


        x1 = xb + 100
        y1 = 100
        x2 = x1 + 400
        y2 = 200
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#0776A0", outline="#FF8500", width=3)



    def canvas_interaction(self, event):
        if event.x > 50 and event.x < 500:
            if event.y > 100 and event.y < 200:
                print('You clicked the magic area')


    def makeTransactionWindow(self):
        w = AddTransaction(self)



    def searchDatabase(self, event):
        print("The user entered ---->", self.contents.get())
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
        w = AddUser(self)


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
        self.username = self.nicknameEntryVariable
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
