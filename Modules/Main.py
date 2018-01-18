import tkinter

class Main:
    def __init__(self, parent):
        self.parent = parent
        self.canvasElements = []

        self.allInfoLabelVariable = 'Account Name: Something Here\nAccount Balance: $100'


def main_window(self):
    geo = str(self.canvasWidth) + 'x' + str(self.canvasHeight) + '+10+30'
    self.master.geometry(geo)
    topFrame = tkinter.Frame(self)
    topFrame.grid(row=0, column=0)
    self.canvas = tkinter.Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
    self.canvas.grid(in_=topFrame, row=0, column=0)

    self.canvas.create_rectangle( 50, 100, 150, 200, fill="#0776A0", outline="#FF8500", width=3)


    bottomFrame = tkinter.Frame(self)
    bottomFrame.grid(row=1, column=0)

    settingsButton = tkinter.Button(self, text='Settings Manager', command = self.options)
    settingsButton.grid(in_=bottomFrame, row=0, column=0)

    transactionButton = tkinter.Button(self, text='Transaction Manager', command = self.makeTransactionWindow)
    transactionButton.grid(in_=bottomFrame, row=0, column=1)

    infoButton = tkinter.Button(self, text='Info', command = self.launch_info_window)
    infoButton.grid(in_=bottomFrame, row=0, column=2)





def main_window_NUM2(self):
    #Top Frame UI Components =============================
    self.topFrame = tkinter.Frame(self)
    self.topFrame.grid(row=0, column=0)
    # Welcome Note
    self.welcomeLabel = tkinter.Label(self, text='Welcome ' + self.userName)
    self.welcomeLabel.grid(in_=self.topFrame, row=0, column=0)
    # Search Entry
    self.searchEntry = tkinter.Entry(self)
    self.searchEntry.grid(in_=self.topFrame, row=0, column=1, padx=400)
    # Options Button
    self.optionsButton = tkinter.Button(self, text='Options', command=self.options)
    self.optionsButton.grid(in_=self.topFrame, row=0, column=2)

    # Middle Frame UI Components ===========================
    self.middleFrame = tkinter.Frame(self)
    self.middleFrame.grid(row=1, column=0)

    # Middle Left Frame
    self.middleLeftFrame = tkinter.Frame(self)
    self.middleLeftFrame.grid(in_=self.middleFrame, row=0, column=0, padx=20)

    # Middle, Accounts Frame
    self.middleAccountsFrame = tkinter.Frame(self)
    self.middleAccountsFrame.grid(in_=self.middleLeftFrame, row=0, column=0, pady=20)
    self.accountsLabel = tkinter.Label(self, text='Select Account')
    self.accountsLabel.grid(in_=self.middleAccountsFrame, row=0, column=0)

    self.accountSelectionVariable = tkinter.StringVar(self)
    self.accountSelectionVariable.set('No Accounts Found')
    self.accountDropDown = tkinter.OptionMenu(self, self.accountSelectionVariable, *self.accounts)
    self.accountDropDown.grid(in_=self.middleAccountsFrame, row=1, column=0)

    #Middle, Transactions Frame
    self.middleTransactionsFrame = tkinter.Frame(self)
    self.middleTransactionsFrame.grid(in_=self.middleLeftFrame, row=1, column=0, pady=20)
    # Label
    self.transactionsLabel = tkinter.Label(self, text='Recent Transactions')
    self.transactionsLabel.grid(in_=self.middleTransactionsFrame, row=0, column=0)
    # Listbox
    self.transactionsListbox = tkinter.Listbox(self)
    self.transactionsListbox.grid(in_=self.middleTransactionsFrame, row=1, column=0, ipadx=30, ipady=60)
    #https://stackoverflow.com/questions/6554805/getting-a-callback-when-a-tkinter-listbox-selection-is-changed

    # Middle Middle Frame
    self.middleMiddleFrame = tkinter.Frame(self)
    self.middleMiddleFrame.grid(in_=self.middleFrame, row=0, column=1, padx=20)
    self.allInfoLabel = tkinter.Label(self, text=self.allInfoLabelVariable)
    self.allInfoLabel.grid(in_=self.middleMiddleFrame, row=0, column=0)

    #Middle Right Frame
    self.middleRightFrame = tkinter.Frame(self)
    self.middleRightFrame.grid(in_=self.middleFrame, row=0, column=2)
    self.canvas = tkinter.Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
    self.canvas.grid(in_=self.middleRightFrame, row=0, column=0)

    # Bottom Frame ==================================
    self.bottomFrame = tkinter.Frame(self)
    self.bottomFrame.grid(row=2, column=0, pady=20)
    # Transaction Button
    self.transactionButton = tkinter.Button(self, text='Add Transaction', command = self.makeTransactionWindow)
    self.transactionButton.grid(in_=self.bottomFrame, row=0, column=0)

    # Other Application Variables
    self.contents = tkinter.StringVar()
    self.contents.set("Search Database...")
    self.searchEntry["textvariable"] = self.contents
    self.searchEntry.bind('<Key-Return>', self.searchDatabase)
