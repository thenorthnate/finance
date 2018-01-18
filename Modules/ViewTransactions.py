import tkinter

class ViewTransactions:
    def __init__(self, parent):
        self.parent = parent
        #Top Level Widgets
        self.transactionWindow = tkinter.Toplevel(parent)
        self.transactionWindow.title('Transactions')
        self.transactionWindow.geometry('500x500+1000+50')


        topFrame = tkinter.Frame(self.transactionWindow)
        topFrame.grid(row=0, column=0, padx=30, pady=30)

        self.searchEntry = tkinter.Entry(self.transactionWindow)
        self.searchEntry.grid(in_=topFrame, row=0, column=0)

        self.transactionsListbox = tkinter.Listbox(self.transactionWindow)
        self.transactionsListbox.grid(in_=topFrame, row=1, column=0, ipadx=30, ipady=60)
        #https://stackoverflow.com/questions/6554805/getting-a-callback-when-a-tkinter-listbox-selection-is-changed


        bottomFrame = tkinter.Frame(self.transactionWindow)
        bottomFrame.grid(row=1, column=0, padx=30, pady=30)

        addTransactionButton = tkinter.Button(self.transactionWindow, text='Add Transaction', command = self.parent.makeTransactionWindow)
        addTransactionButton.grid(in_=bottomFrame, row=1, column=0)

        self.transactionWindow.state('withdrawn')
