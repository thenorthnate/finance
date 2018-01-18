import tkinter

class Login:
    def __init__(self, parent):
        self.parent = parent
        self.loginWindow = tkinter.Toplevel(parent)
        self.loginWindow.title('Login')
        #loginWindow.geometry('500x500+400+100')

        topFrame = tkinter.Frame(self.loginWindow)
        packConfig = parent.config['login']['component']['topFrame']
        topFrame.grid(row=packConfig['row'], column=packConfig['column'], padx=packConfig['padx'], pady=packConfig['pady'])
        photoPath = parent.cwd + '/Static/Images/lock.gif'
        photo = tkinter.PhotoImage(file=photoPath)
        loginPhotoLabel = tkinter.Label(self.loginWindow, image=photo)
        loginPhotoLabel.image = photo # keep a reference!
        packConfig = parent.config['login']['component']['loginPhotoLabel']
        loginPhotoLabel.grid(in_=topFrame, row=packConfig['row'], column=packConfig['column'])



        bottomFrame = tkinter.Frame(self.loginWindow)
        bottomFrame.grid(row=1, column=0, pady=10)


        self.loginEntry = tkinter.Entry(self.loginWindow)
        self.loginEntry.grid(in_=bottomFrame, row=0, column=0)

        # self.loginEntry["textvariable"] = self.parent.loginContents
        self.loginEntry.insert(0, "Username...")
        self.loginEntry.bind('<Key-Return>', self.login_callback)
        self.loginEntry.bind('<Button-1>', self.clear_text)

        self.loginWindow.bind("<Button-1>", self.click_callback)

    def login_callback(self, event):
        userEntry = self.loginEntry.get()
        self.loginEntry.delete(0, tkinter.END)
        if self.parent.username == '':
            self.parent.username = userEntry
            self.loginEntry.config(show='*')
        else:
            self.parent.password = userEntry

        if self.parent.username != '' and self.parent.password != '':
            self.parent.loggedIn = True
            self.loginWindow.state('withdrawn')
            self.parent.master.state('normal')
            self.parent.transactionWindow.transactionWindow.state('normal')

    def clear_text(self, event):
        self.loginEntry.delete(0, tkinter.END)

    def click_callback(self, event):
        print('X: ' + str(event.x))
        print('Y: ' + str(event.y))
