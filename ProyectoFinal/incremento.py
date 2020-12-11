import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font

from PIL import Image, ImageTk

import sqlite3


conn = sqlite3.connect('pruebas.db')
c = conn.cursor()

print(c.execute("insert into ejemplo values (NULL, 'holi')"))
conn.commit()

