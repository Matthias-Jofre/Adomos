import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font

from PIL import Image,ImageTk

import sqlite3

db_name = 'database.db'


def mostrarFrecuencia():
    print(radioLeido.get())

def mostrarDiametro():
    print(radioLeido2.get())    

def mostrarTipo():
    print(radioLeido3.get())  

def run_query(query, parameters = ()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

def get_usuario(rut, contraseña):
    query = 'SELECT rut FROM usuario_p WHERE rut = ? AND contraseña = ?'
    parametros = (rut, contraseña)
    run_query(query, parametros)
    entrada_1.delete(0, END)
    entrada_2.delete(0, END)


def agregarDomo():
    query = 'INSERT INTO domos VALUES(NULL, ?, ?, ?)'
    fre = radioLeido.get()
    dia = radioLeido2.get()
    tip = radioLeido3.get()
    parametros = (fre, dia, tip)
    run_query(query, parametros)
    print(parametros)

####Ventana principal ############################
ventana = Tk()
ventana.title("GeodesikApp")
ventana.geometry('1600x900')
ventana.config(bg="black")
########## FIJAR VENTANA ##########################
ventana.resizable(0, 0)
backFrame = Frame(master=ventana)
backFrame.pack()
backFrame.propagate(0)
###################################################
# Background
img = PhotoImage(file = "./imagenes/fondo_2.png")
etiquetaIcono = Label(ventana,image=img)
etiquetaIcono.pack()
###################################################
Fuente_0 = font.Font(family="Bradley Hand ITC", size=30, weight="bold")
Fuente_01 = font.Font(family="Bradley Hand ITC", size=20, weight="bold")
Fuente_02 = font.Font(family="Times New Roman", size=8, weight="bold")
Fuente_1 = font.Font(family="Times New Roman", size=20, weight="bold")
Fuente_2 = font.Font(family="Calibri", size=19, weight="bold")
Fuente_3 = font.Font(family="Times New Roman", size=15, weight="bold")
Fuente_4 = font.Font(family="Times New Roman", size=12, weight="bold")
###################################################
rec_log = Canvas(ventana, width=350, height=350)
rec_log.create_rectangle(0, 0, 350, 350, fill="black", outline = "black")
rec_log.place(x = 30, y = 30)

rec_inf = Canvas(ventana, width=350, height=460)
rec_inf.create_rectangle(0, 0, 350, 460, fill="black", outline = "black")
rec_inf.place(x = 30, y = 400)

rec_dom = Canvas(ventana, width=1000, height=650)
rec_dom.create_rectangle(0, 0, 1000, 650, fill="white", outline = "white")
rec_dom.place(x = 500, y = 60)

#####cargando imagenes y entradas de ventana ventas
img_frec2 = Image.open('./imagenes/frec2.png')
img_frec2 = ImageTk.PhotoImage(img_frec2)

img_frec4 = Image.open('./imagenes/frec4.png')
img_frec4 = ImageTk.PhotoImage(img_frec4)

img_frec6 = Image.open('./imagenes/frec6.png')
img_frec6 = ImageTk.PhotoImage(img_frec6)

Label(ventana,font=Fuente_3, image=img_frec2,fg="black",text="Limpiar",bg="white").place(x=658,y=163)
Label(ventana,font=Fuente_3, image=img_frec4,fg="black",text="Limpiar",bg="white").place(x=933,y=170)
Label(ventana,font=Fuente_3, image=img_frec6,fg="black",text="Limpiar",bg="white").place(x=1208,y=170)

titulo_carac = Label(ventana, font = Fuente_4, text="Caracteristicas del Domo", bg= "white", fg="black")
titulo_carac.place(x=880,y=70)

titulo_frecuencias = Label(ventana, font = Fuente_4, text="Seleccione la frecuencia, diametro y tipo: ", bg= "white", fg="black")
titulo_frecuencias.place(x=520,y=120)

radioLeido = IntVar() 
frec1 = Radiobutton(ventana,text='Frecuencia 2',variable=radioLeido, value=350000, bg="white", command=mostrarFrecuencia, padx =20, pady =10) 
frec2 = Radiobutton(ventana,text='Frecuencia 4',variable=radioLeido, value=700000, bg="white", command=mostrarFrecuencia, padx =20, pady =10) 
frec3 = Radiobutton(ventana,text='Frecuencia 6',variable=radioLeido, value=1000000, bg="white", command=mostrarFrecuencia, padx =20, pady =10) 
frec1.place(x=657,y=270)
frec2.place(x=935,y=270)
frec3.place(x=1208,y=270)

radioLeido2 = IntVar() 
diam1 = Radiobutton(ventana,text='5 metros',variable=radioLeido2, value=5, bg="white", command=mostrarDiametro, padx =34, pady =10) 
diam2 = Radiobutton(ventana,text='10 metros',variable=radioLeido2, value=10, bg="white", command=mostrarDiametro, padx =30, pady =10) 
diam3 = Radiobutton(ventana,text='15 metros',variable=radioLeido2, value=15, bg="white", command=mostrarDiametro, padx =30, pady =10) 
diam1.place(x=657,y=350)
diam2.place(x=935,y=350)
diam3.place(x=1208,y=350)

radioLeido3 = StringVar() 
tipo1 = Radiobutton(ventana,text='Habitacional',variable=radioLeido3, value="habitacional", bg="white", command=mostrarTipo, padx =20, pady =10) 
tipo2 = Radiobutton(ventana,text='Invernadero',variable=radioLeido3, value="invernadero", bg="white", command=mostrarTipo, padx =23, pady =10) 
tipo3 = Radiobutton(ventana,text='Exposición',variable=radioLeido3, value="exposicion", bg="white", command=mostrarTipo, padx =27, pady =10) 
tipo1.place(x=657,y=430)
tipo2.place(x=935,y=430)
tipo3.place(x=1208,y=430)

ingresar_domo = Button(ventana, text="Registrar Domo", padx =100, pady =10, bg = "white", command = agregarDomo())
ingresar_domo.place(x=860, y=500)

###################################################

Label(ventana, font = Fuente_0, text="Geodesi-K", bg= "black", fg="white").place(x=90,y=40)
Label(ventana, font = Fuente_01, text="Ingresar", bg= "black", fg="white").place(x=100,y=110)
Label(ventana, font = Fuente_4, text="Rut Usuario: ", bg= "black", fg="white").place(x=100,y=180)

entrada_1 = Entry(ventana)
entrada_1.focus()
entrada_1.place(x=115, y=210)

Label(ventana, font = Fuente_4, text="Contraseña: ", bg= "black", fg="white").place(x=100,y=250)

entrada_2 = Entry(ventana, show="*")
entrada_2.place(x=115, y=280)

boton_1 = Button(ventana, text="Ingresar", command = lambda: get_usuario(entrada_1.get(), entrada_2.get()))
boton_1.place(x=150, y=320)

Label(ventana, font = Fuente_3, text="Datos de usuario", bg= "black", fg="white").place(x=100,y=420)
Label(ventana, font = Fuente_4, text="Nombre", bg= "black", fg="white").place(x=50,y=480)
entrada_3 = Entry(ventana)
entrada_3.place(x=160, y=480)
Label(ventana, font = Fuente_4, text="Apellido", bg= "black", fg="white").place(x=50,y=520)
entrada_4 = Entry(ventana)
entrada_4.place(x=160, y=520)
Label(ventana, font = Fuente_4, text="Rut", bg= "black", fg="white").place(x=50,y=560)
entrada_5 = Entry(ventana)
entrada_5.place(x=160, y=560)
Label(ventana, font = Fuente_4, text="Correo", bg= "black", fg="white").place(x=50,y=600)
entrada_6= Entry(ventana)
entrada_6.place(x=160, y=600)
Label(ventana, font = Fuente_4, text="Telefono", bg= "black", fg="white").place(x=50,y=640)
entrada_7 = Entry(ventana)
entrada_7.place(x=160, y=640)
 
ventana.mainloop()
