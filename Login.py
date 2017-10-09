from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Register import *
from Recovery import *
from Main import *
from Settings import *

class Login:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Login')

        self.logLab = Label(self.master, text = 'Login', bg = 'white', font = 'Verden 14')
        self.logEnt = Entry(self.master)
        self.logLab.grid(row = 1, column = 1)
        self.logEnt.grid(row = 1, column = 3)

        self.passLab = Label(self.master, text = 'Password', bg = 'white', font = 'Verden 14')
        self.passEnt = Entry(self.master)
        self.passLab.grid(row = 2, column = 1)
        self.passEnt.grid(row = 2, column = 3)

        self.logBtn = Button(self.master, text = 'Login', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.logOnClick)
        self.regBtn = Button(self.master, text = 'Register', width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command = self.regOnClick)
        self.recBtn = Button(self.master, text = 'Forgot password or login', width = 20, bg = 'red', font = 'Verden 14', fg = 'white', command = self.recOnClick)
        self.logBtn.grid(row = 3, column = 1, columnspan = 3)
        self.regBtn.grid(row = 4, column = 1, columnspan = 3)
        self.recBtn.grid(row = 5, column = 1, columnspan = 3)

    def verify(self):
        file = open('regDB.txt', 'r')
        logPass = file.read()

        login = self.logEnt.get()
        password = self.passEnt.get()

        if login is '' or password is '':
            return False

        for i in range(len(logPass)):
            if logPass[i:i+4] == 'Name:':
                i += 4
                continue
            else:
                if logPass[i:i+len(login)] == login:
                    if logPass[i+len(login)+11:i+len(login)+11+len(password)] == password:
                        return True

                if logPass[i:i+len(login)] != login:
                    i += len(login) + 21 + len(password)

                if i == len(logPass):
                    return False

    def regOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Register(self.newWindow)

    def logOnClick(self):
        if self.verify():
            self.newWindow = tk.Toplevel(self.master)
            self.app = Main(self.newWindow)
        else:
            messagebox.showerror('Error', 'Invalid login or password')

    def recOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Recovery(self.newWindow)

def main():
    window = tk.Tk()
    app = Login(window)
    window.mainloop()

if __name__ == '__main__':
    main()
