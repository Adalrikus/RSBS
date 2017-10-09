from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Settings:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title('Settings')
