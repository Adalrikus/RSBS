from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Recovery:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.configure(background = 'white')
        self.master.title('Recovery')

        self.logRecBtn = Button(self.master, text = 'Recover login', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.logRecOnClick)
        self.pasRecBtn = Button(self.master, text = 'Recover password', width = 20, bg = 'green', font = 'Verden 14', fg = 'white', command = self.pasRecOnClick)
        self.logRecBtn.grid(row = 1, column = 1)
        self.pasRecBtn.grid(row = 2, column = 1)

    def logRecOnClick(self):
        self.logRecBtn.destroy()
        self.pasRecBtn.destroy()

        self.logRecLab = Label(self.master, text = 'Recover login', bg = 'white', font = 'Verden 14')
        self.logRecLab.grid(row = 1, column = 1, columnspan = 2)

        self.secLab = Label(self.master, text = 'Enter your secret word', bg = 'white', font = 'Verden 14')
        self.secEnt = Entry(self.master)
        self.secLab.grid(row = 2, column = 1)
        self.secEnt.grid(row = 2, column = 2)

        self.recBtn = Button(self.master, text = 'Recover login', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white')
        self.recBtn.grid(row = 3, column = 1, columnspan = 2)

    def pasRecOnClick(self):
        self.pasRecBtn.destroy()
        self.logRecBtn.destroy()

        self.pasRecLab = Label(self.master, text = 'Recover password', bg = 'white', font = 'Verden 14')
        self.pasRecLab.grid(row = 1, column = 1, columnspan = 2)

        self.secLab = Label(self.master, text = 'Enter your secret word', bg = 'white', font = 'Verden 14')
        self.secEnt = Entry(self.master)
        self.secLab.grid(row = 2, column = 1)
        self.secEnt.grid(row = 2, column = 2)

        self.recBtn = Button(self.master, text = 'Recover login', width = 20, bg = 'blue', font = 'Verden 14', fg = 'white')
        self.recBtn.grid(row = 3, column = 1, columnspan = 2)
