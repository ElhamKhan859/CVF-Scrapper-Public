import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import datetime
from ctypes import windll
import scrap_website
import threading
from threading import Thread
import sys





class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CVF Open Access Downloader")
        self.iconbitmap(r'C:\Users\Moh_N\Downloads\PaperDownloader\cvf.ico')
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.style.theme_use('xpnative') # another good one is 'vista'

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.style = ttk.Style()
        self.style.configure("Intro.TLabel", 
            font=("Arial", 14, "bold"),
            background="#f0f0f0",  # Light gray background
            foreground="#333",     # Dark gray text color
            padding=10)

        self.intro_label = ttk.Label(self, text='Bulk Download Open-Access Papers From CVF', style='Intro.TLabel', anchor='center')
        self.intro_label.grid(row=0, column=0, padx= 5, pady=5, sticky='we', columnspan=3)

        self.style_year = ttk.Style()
        self.style_year.configure("YearLabel.TLabel", 
                    font=("Arial", 12),
                    foreground="#333",       # Dark gray text color
                    padding=5) 

        self.year_label = ttk.Label(self, text="Download papers published from the year (year included) onwards: ",style="YearLabel.TLabel", anchor='center')
        self.year_label.grid(row=1, column=0, padx=10, pady=5, sticky='we', columnspan=3)


""" 

Contact developer for the rest of the source code

"""