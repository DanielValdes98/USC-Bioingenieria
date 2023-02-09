from calendar import Calendar, month
from os import close
from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import random
import numpy as np
from tkcalendar import *

import tkSimpleDialog

class CalendarDialog(tkSimpleDialog.Dialog): 
    """Dialog box that displays a calendar and returns the selected date""" 
    def body(self, master): 
        self.calendar = calendar.Calendar(master) 
        self.calendar.pack() 

    def apply(self): 
        elf.result = self.calendar.selection 

# Demo code: 
def main(): 
    root = tk.Tk() 
    root.wm_title("CalendarDialog Demo") 

    def onclick(): 
        cd = CalendarDialog(root) 
        print cd.result 

        button = Button(root, text="Click me to see a calendar!", command=onclick) 
        button.pack() 
        root.update() 

        root.mainloop() 


if __name__ == "__main__": 
    main() 