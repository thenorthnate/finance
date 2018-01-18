import tkinter

class AddUser:
    def __init__(self, parent):
        window = tkinter.Toplevel(parent)
        window.title('Add User')
        window.geometry('500x500+400+100')

        print(parent.username)


    def add_user_window(self):
        #EDIT!!!!!
        self.optionsWindow.withdraw()
        self.addUserWindow = tkinter.Toplevel(self)
        self.addUserWindow.title('Add User')
        self.addUserWindow.geometry('500x500+400+100')


        # First Name
        self.firstNameEntry = tkinter.Entry(self.addUserWindow)
        self.firstNameEntry.grid(in_=self.addUserWindow, row=0, column=0)
        self.firstNameEntryVariable = tkinter.StringVar()
        self.firstNameEntryVariable.set('')
        self.firstNameEntry["textvariable"] = self.firstNameEntryVariable
        # Last Name
        self.lastNameEntry = tkinter.Entry(self.addUserWindow)
        self.lastNameEntry.grid(in_=self.addUserWindow, row=1, column=0)
        self.lastNameEntryVariable = tkinter.StringVar()
        self.lastNameEntryVariable.set('')
        self.lastNameEntry["textvariable"] = self.lastNameEntryVariable
        # Nickname
        self.nicknameEntry = tkinter.Entry(self.addUserWindow)
        self.nicknameEntry.grid(in_=self.addUserWindow, row=2, column=0)
        self.nicknameEntryVariable = tkinter.StringVar()
        self.nicknameEntryVariable.set('')
        self.nicknameEntry["textvariable"] = self.nicknameEntryVariable

        self.emailEntry = tkinter.Entry(self.addUserWindow)
        self.emailEntry.grid(in_=self.addUserWindow, row=3, column=0)
        self.emailEntryVariable = tkinter.StringVar()
        self.emailEntryVariable.set('')
        self.emailEntry["textvariable"] = self.emailEntryVariable

        self.passwordEntry = tkinter.Entry(self.addUserWindow)
        self.passwordEntry.grid(in_=self.addUserWindow, row=4, column=0)
        self.passwordEntryVariable = tkinter.StringVar()
        self.passwordEntryVariable.set('')
        self.passwordEntry["textvariable"] = self.passwordEntryVariable

        self.birthdayEntry = tkinter.Entry(self.addUserWindow)
        self.birthdayEntry.grid(in_=self.addUserWindow, row=5, column=0)
        self.birthdayEntryVariable = tkinter.StringVar()
        self.birthdayEntryVariable.set('')
        self.birthdayEntry["textvariable"] = self.birthdayEntryVariable

        self.submitNewUserButton = tkinter.Button(self.addUserWindow, text='Submit', command=self.submitUser)
        self.submitNewUserButton.grid(in_=self.addUserWindow, row=6, column=0)
        self.cancelNewUserButton = tkinter.Button(self.addUserWindow, text='Cancel', command=self.cancelNewUser)
        self.cancelNewUserButton.grid(in_=self.addUserWindow, row=7, column=0)
