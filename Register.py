from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Register:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Register')

        self.usrLab = Label(self.master, text = "Username", bg = 'white', font = 'Verden 14')
        self.usrEnt = Entry(self.master)
        self.usrLab.grid(row = 1, column = 1)
        self.usrEnt.grid(row = 1, column = 3)

        self.passLab = Label(self.master, text = "Password", bg = 'white', font = 'Verden 14')
        self.passEnt = Entry(self.master)
        self.passLab.grid(row = 2, column = 1)
        self.passEnt.grid(row = 2, column = 3)

        self.secLab = Label(self.master, text = "Secret word", bg = 'white', font = 'Verden 14')
        self.secEnt = Entry(self.master)
        self.secLab.grid(row = 3, column = 1)
        self.secEnt.grid(row = 3, column = 3)

        self.regBtn = Button(self.master, text = "Register", width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command = self.regOnClick)
        self.regBtn.grid(row = 4, column = 1, columnspan = 3)

    def exist(self):
        file = open('regDB.txt', 'r')
        logPass = file.read()

        login = self.usrEnt.get()
        password = self.passEnt.get()
        secret = self.secEnt.get()

        for i in range(len(logPass)):
            if logPass[i:i+4] == 'Name:':
                i += 4
                continue
            else:
                if logPass[i:i+len(login)] == login:
                    return True

                if logPass[i:i+len(login)] != login:
                    i += len(login) + 21 + len(password) + len(secret)

                if i == len(logPass):
                    return False

    def regOnClick(self):
        self.login = self.usrEnt.get()
        self.password = self.passEnt.get()
        self.secret = self.secEnt.get()

        if not self.exist():
            file = open('regDB.txt', 'a')
            file.write('Name: ' + self.login + ' Password: ' + self.password + ' Secret: ' + self.secret + ' ')
        else:
            messagebox.showwarning('Warning', 'This login alerady exists')
