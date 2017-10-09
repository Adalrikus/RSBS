from tkinter import *
import tkinter as tk
from Settings import *

class Main:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('Railway booking system')
        self.master.configure(background = 'white')

        self.btnSet = Button(self.master, text = 'Settings', width = 10, bg = 'blue', font = 'Verden 14', fg = 'white', command = self.setOnClick)
        self.btnSet.grid(row = 0, column = 0)

        self.trnLab = Label(self.master, text = 'Train #', bg = 'white', font = 'Verden 14')
        self.trnLst = Listbox(self.master)
        self.trnLab.grid(row = 0, column = 1)
        self.trnLst.grid(row = 0, column = 2)
        self.trnLst.full()

        self.btnBk = Button(self.master, text = 'Booking', width = 10, bg = 'purple', font = 'Verden 14', fg = 'white', command = self.bkOnClick)
        self.btnBk.grid(row = 1, column = 1, columnspan = 2)

    def setOnClick(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Settings(self.newWindow)

    def bkOnClick(self):
        file = open('bookDB.txt', 'a')

    def full(self):
        for i in range(10):
            self.trnLst.instert(END, i)
