from tkinter import ttk
from tkinter import *

import sqlite3

class Pruebas:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        

if __name__ == '__main__':
    window = Tk()
    application = Pruebas(window)
    window.mainloop()    

