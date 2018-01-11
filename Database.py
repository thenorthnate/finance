#Database Class
#Nathan North
#Supports the cotton application

import sqlite3, time

class Database:
    def __init__(self):
        self.accountNumber = None
        self.type = None
        self.value = None
        self.error = None
        self.latestTransactionId = 0

        self.conn = sqlite3.connect('cotton.db')
        self.c = self.conn.cursor()



    def createTables(self):
        try: #Make these check for existance! Not just error catching!!!
            self.c.execute("CREATE TABLE transactions (id integer, transactionDay integer, transactionMonth integer, transactionYear integer, accountNumber integer, tag text, type text, amount real, description text, timestamp integer)")
            self.conn.commit()
        except:
            pass
        try:
            self.c.execute('''CREATE TABLE accounts (bankName text, quickID text, accountNumber integer, accountType integer, creationDate text, balance real)''')
            self.conn.commit()
        except:
            pass
        try:
            self.c.execute('''CREATE TABLE users (userID text, firstName text, lastName text, nickName text, email text, password text, birthdate text)''')
            self.conn.commit()
        except:
            pass
        try:
            self.c.execute("CREATE TABLE accountTypes (shortName text, longName text)")
            self.conn.commit()
            biAccounts = [('CH', 'CHECKING'), ('SA', 'SAVINGS'), ('CD', 'CD'), ('HSA', 'HEALTH SAVINGS ACCOUNT'), ('401K', '401K')]
            for item in biAccounts:
                self.c.execute("INSERT INTO accountTypes VALUES" + str(item))
                self.conn.commit()
        except:
            pass
        try:
            self.c.execute("CREATE TABLE tags (tag text, description text)")
            self.conn.commit()
            biTags = [('R', 'RENT'), ('CC', 'CREDIT CARD'), ('C', 'CAR'), ('M', 'MISCELLANEOUS')]
            for item in biTags:
                self.c.execute("INSERT INTO tags VALUES" + str(item))
                self.conn.commit()
        except:
            pass

    def getLastTransactionId(self):
        self.c.execute('''SELECT MAX(id) FROM transactions''')
        self.latestTransactionId = self.c.fetchone()

    def addUser(self, entry):
        try:
            ex = "INSERT INTO users VALUES " + str(entry)
            self.c.execute(ex)
            self.conn.commit()
        except:
            self.createTables()
            ex = "INSERT INTO users VALUES " + str(entry)
            self.c.execute(ex)
            self.conn.commit()
