#pip install sqlite
import sqlite3
from sqlite3 import Error

#pip install pandasgui
from pandasgui import show

#pip install Numpy
import numpy as np

#pip install matplotlib --- pylab
import pylab as pl

from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox

#pip install Pillow
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import font
from time import sleep
import time
from datetime import date
from datetime import datetime

def validarUsuario():
    if entrada_1.get() == 'matt':
        abrirventanUsuario()
        ventana.withdraw()
    else:
        messagebox.showwarning("Error", "Usuario no valido")

def validarAdministrador():
    if entrada_2.get() == 'matt':
        abrirVentanaAdministrador()
        ventana.withdraw()
    else:
        messagebox.showwarning("Error", "Administrador no valido")

def reponerventana():
    ventana.deiconify()
    win.destroy()

def reponerventana2():
    ventana.deiconify()
    v_admin.destroy()

def abrirVentanaPresupuesto():
    
    def mostrarFrecuencia():
        print(radioLeido.get())
    
    #VENTANA PRINCIPAL.
    root = tk.Toplevel()
    root.title("Presupuesto")
    root.geometry("565x600")

    root.resizable(0, 0)
    backFrame = Frame(master=root)
    backFrame.pack()
    backFrame.propagate(0)

    #INCLUIMOS PANEL PARA LAS PESTAÑAS.
    nb = ttk.Notebook(root)
    nb.pack(fill='both',expand='yes')

    #CREAMOS PESTAÑAS
    p1 = Frame(nb, background="white")
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)

    Etiqueta_1= Label(p1,fg="black",font=Fuente_01,text="Tipo de frecuencia",bg="white").place(x=160,y=10)

    Etiqueta_4= Label(p1,fg="black",font=Fuente_01,text="Diametro",bg="white").place(x=160,y=300)

    Etiqueta_6= Label(p1,fg="black",font=Fuente_01,text="Tipos de madera",bg="white").place(x=160,y=180)
    
    ########Option Menu###############################################
    var = tk.StringVar(p1)
    var.set('Maderas blandas')
    oprciones_madera = ['Pino','Álamo', 'Abeto']
    opcion = tk.OptionMenu(p1, var, *oprciones_madera)
    opcion.config(width=20)
    opcion.place(x=100,y=230)

    var2 = tk.StringVar(p1)
    var2.set('Maderas duras')
    oprciones_madera2 = ['Roble','Caoba', 'Nogal']
    opcion = tk.OptionMenu(p1, var2, *oprciones_madera2)
    opcion.config(width=20)
    opcion.place(x=300,y=230)

    var3 = tk.IntVar(p1)
    var3.set('En metros')
    oprciones_diametro = [5, 15, 20]
    opcion = tk.OptionMenu(p1, var3, *oprciones_diametro)
    opcion.config(width=20)
    opcion.place(x=300,y=305)

    Etiqueta_9= Label(p1,fg="black",font=Fuente_01,text="Mano de obra",bg="white").place(x=110,y=370)

    imagen_frec2 = Label(p1,font=Fuente_3, image=img_frec2,fg="black",text="Limpiar",bg="white").place(x=10,y=55)

    imagen_frec4 = Label(p1,font=Fuente_3, image=img_frec4,fg="black",text="Limpiar",bg="white").place(x=200,y=63)

    imagen_frec6 = Label(p1,font=Fuente_3, image=img_frec6,fg="black",text="Limpiar",bg="white").place(x=400,y=63)

    radioLeido = IntVar() 
    frec1 = Radiobutton(p1,text='Frecuencia 2',variable=radioLeido, value=350000, bg="white", command=mostrarFrecuencia) 
    frec2 = Radiobutton(p1,text='Frecuencia 4',variable=radioLeido, value=700000, bg="white", command=mostrarFrecuencia) 
    frec3 = Radiobutton(p1,text='Frecuencia 6',variable=radioLeido, value=1000000, bg="white", command=mostrarFrecuencia) 
    frec1.place(x=30,y=140)
    frec2.place(x=225,y=140)
    frec3.place(x=423,y=140)

    radioLeido2 = IntVar()
    obra_si = Radiobutton(p1,text='Si',variable=radioLeido2, value=bool, bg="white") 
    obra_no = Radiobutton(p1,text='No',variable=radioLeido2, value=bool, bg="white") 
    obra_si.place(x=300,y=377)
    obra_no.place(x=350,y=377)

    boton_presupuestar = Button(p1,font=Fuente_3, image=img_presupuesto,fg="black",text="Limpiar",bg="white").place(x=140,y=450)

    entry_pres = ttk.Entry(p1, textvariable=entry_var_pres, state="readonly").place(x=210,y=453,width=250, height=50)

    Label(p2,fg="black",font=Fuente_1,text="Datos de contacto").place(x=10,y=10)
    Label(p2,fg="black",font=Fuente_3,text="Nombre").place(x=10,y=70)
    Label(p2,fg="black",font=Fuente_3,text="Rut").place(x=10,y=100)
    Label(p2,fg="black",font=Fuente_3,text="Telefono").place(x=10,y=130)
    Label(p2,fg="black",font=Fuente_3,text="Dirección").place(x=10,y=160)
    Label(p2,fg="black",font=Fuente_3,text="Correo").place(x=10,y=190)

    Entry(p2).place(x=150,y=75)
    Entry(p2).place(x=150,y=105)
    Entry(p2).place(x=150,y=135)
    Entry(p2).place(x=150,y=165)
    Entry(p2).place(x=150,y=195)

    Button(p2, text="Ingresar Datos", fg="Black").place(x=170,y=240)

    Label(p3,fg="black",font=Fuente_1,text="Método de pago y envio").place(x=10,y=10)
    Label(p3,fg="black",font=Fuente_3,text="Forma de pago").place(x=10,y=70)
    Label(p3,fg="black",font=Fuente_3,text="Recibe").place(x=10,y=100)
    Label(p3,fg="black",font=Fuente_3,text="Método de envio").place(x=10,y=130)
    Label(p3,fg="black",font=Fuente_3,text="Dirección de envio").place(x=10,y=160)
    Label(p3,fg="black",font=Fuente_3,text="Tiempo estimado").place(x=10,y=190)

    Entry(p3).place(x=180,y=75)
    Entry(p3).place(x=180,y=105)
    Entry(p3).place(x=180,y=135)
    Entry(p3).place(x=180,y=165)
    Entry(p3).place(x=180,y=195)

    Button(p3, text="Validar Datos", fg="Black").place(x=170,y=240)

    nb.add(p1,text='Especificaciones')
    nb.add(p2,text='Registro')
    nb.add(p3,text='Pago y Despacho')

def abrirVentasUsuario():
    v_usuario = tk.Toplevel()
    v_usuario.title("PresuDomo")
    v_usuario.geometry("300x350")
    v_usuario.config(bg="white")

    v_usuario.resizable(0, 0)
    backFrame = Frame(master=v_usuario)
    backFrame.pack()
    backFrame.propagate(0)

    Label(v_usuario,fg="black",font=Fuente_2,text="Estadisticas Generales", bg ="white").place(x=10,y=10)
    Label(v_usuario,fg="black",font=Fuente_3,text="Mayor venta:", bg ="white").place(x=10,y=70)
    Label(v_usuario,fg="black",font=Fuente_3,text="Menor venta:", bg ="white").place(x=10,y=100)
    Label(v_usuario,fg="black",font=Fuente_3,text="Media de ventas:", bg ="white").place(x=10,y=130)
    Label(v_usuario,fg="black",font=Fuente_3,text="Promedio de ventas: ", bg ="white").place(x=10,y=160)
    Label(v_usuario,fg="black",font=Fuente_3,text="Total vendido: ", bg ="white").place(x=10,y=190)

    Button(v_usuario,font=Fuente_3, image=img_actualizar,fg="black",text="Limpiar", bg="white").place(x=110,y=240)

def abrirVentanaAdministrador():
    global v_admin
    v_admin = tk.Toplevel()
    v_admin.title("Administrador")
    v_admin.geometry("300x400")

    v_admin.resizable(0, 0)
    backFrame = Frame(master=v_admin)
    backFrame.pack()
    backFrame.propagate(0)

    #INCLUIMOS PANEL PARA LAS PESTAÑAS.
    nb = ttk.Notebook(v_admin)
    nb.pack(fill='both',expand='yes')

    #CREAMOS PESTAÑAS
    q1 = Frame(nb, background="white")
    q2 = Frame(nb, background="white")
    q3 = Frame(nb, background="white")

    Label(q1,fg="black",font=Fuente_2,text="Estadisticas Generales", bg ="white").place(x=10,y=10)
    Label(q1,fg="black",font=Fuente_3,text="Mayor venta:", bg ="white").place(x=10,y=70)
    Label(q1,fg="black",font=Fuente_3,text="Menor venta:", bg ="white").place(x=10,y=100)
    Label(q1,fg="black",font=Fuente_3,text="Media de ventas:", bg ="white").place(x=10,y=130)
    Label(q1,fg="black",font=Fuente_3,text="Promedio de ventas: ", bg ="white").place(x=10,y=160)
    Label(q1,fg="black",font=Fuente_3,text="Total vendido: ", bg ="white").place(x=10,y=190)

    boton_barra = Button(q1,font=Fuente_3, image=img_barra,fg="black",text="Limpiar",bg="white").place(x=30,y=240)

    boton_torta = Button(q1,font=Fuente_3, image=img_torta,fg="black",text="Limpiar",bg="white").place(x=160,y=240)

    Label(q2,fg="black",font=Fuente_2,text="ID Usuario", bg ="white").place(x=10,y=10)
    Entry(q2).place(x=130,y=15,width=150, height=30)

    Label(q2,fg="black",font=Fuente_3,text="Mayor venta:", bg ="white").place(x=10,y=70)
    Label(q2,fg="black",font=Fuente_3,text="Menor venta:", bg ="white").place(x=10,y=100)
    Label(q2,fg="black",font=Fuente_3,text="Media de ventas:", bg ="white").place(x=10,y=130)
    Label(q2,fg="black",font=Fuente_3,text="Promedio de ventas: ", bg ="white").place(x=10,y=160)
    Label(q2,fg="black",font=Fuente_3,text="Total vendido: ", bg ="white").place(x=10,y=190)

    boton_busqueda = Button(q2,font=Fuente_3, image=img_busqueda,fg="black",text="Limpiar",bg="white").place(x=110,y=240)

    Label(q3,fg="black",font=Fuente_2,text="Añadir nuevo usuario", bg ="white").place(x=10,y=10)
    Label(q3,fg="black",font=Fuente_3,text="Nombre:", bg ="white").place(x=10,y=70)
    Label(q3,fg="black",font=Fuente_3,text="Apellido:", bg ="white").place(x=10,y=100)
    Label(q3,fg="black",font=Fuente_3,text="Rut:", bg ="white").place(x=10,y=130)
    Label(q3,fg="black",font=Fuente_3,text="Cargo: ", bg ="white").place(x=10,y=160)
    Label(q3,fg="black",font=Fuente_3,text="Identificador: ", bg ="white").place(x=10,y=190)

    Entry(q3).place(x=150,y=75)
    Entry(q3).place(x=150,y=105)
    Entry(q3).place(x=150,y=135)
    Entry(q3).place(x=150,y=165)
    Entry(q3).place(x=150,y=195)

    boton_añadir = Button(q3,font=Fuente_3, image=img_añadir,fg="black",text="Limpiar",bg="white").place(x=110,y=240)

    boton_salida = Button(v_admin,font=Fuente_3, image=img_salida,fg="black",text="Limpiar",bg="white", command=reponerventana2).place(x=2,y=372)

    nb.add(q1,text='General')
    nb.add(q2,text='Usuario')
    nb.add(q3,text='Añadir')

def abrirventanUsuario():
    
    global win
    win = tk.Toplevel()
    win.title("GeodesikApp")
    win.geometry('566x430')
    win.config(bg="black")

    win.resizable(0, 0)
    backFrame = Frame(master=win)
    backFrame.pack()
    backFrame.propagate(0)

    etiqueta_0 = Label(win, font = Fuente_01, text="Datos de usuario", bg= "black", fg="white").place(x=10,y=15)
    etiqueta_1 = Label(win, font = Fuente_4, text="Nombre: ", bg= "black", fg="white").place(x=35,y=60)
    etiqueta_2 = Label(win, font = Fuente_4, text="Apellido: ", bg= "black", fg="white").place(x=35,y=85)
    etiqueta_3 = Label(win, font = Fuente_4, text="Rut: ", bg= "black", fg="white").place(x=35,y=110)
    etiqueta_4 = Label(win, font = Fuente_4, text="Cargo: ", bg= "black", fg="white").place(x=35,y=135)
    etiqueta_0 = Label(win, font = Fuente_01, text="Operaciones Disponibles", bg= "black", fg="white").place(x=120,y=180)

    boton_Limp = Button(win,font=Fuente_3, image=B_Limpiar,fg="black",text="Limpiar",command=abrirVentanaPresupuesto).place(x=170,y=240)

    boton_Vent = Button(win,font=Fuente_3, image=B_ventas,fg="black",text="Limpiar", command=abrirVentasUsuario).place(x=280,y=240)

    boton_Salir = Button(win,font=Fuente_4,fg="black",text="Desconectar", bg="white", command=reponerventana).place(x=235,y=350)

    entry_nom = ttk.Entry(win, textvariable=entry_var_nom, state="readonly").place(x=110,y=65)

    entry = ttk.Entry(win, textvariable=entry_var_ape, state="readonly").place(x=110,y=90)

    entry = ttk.Entry(win, textvariable=entry_var_rut, state="readonly").place(x=110,y=115)

    entry = ttk.Entry(win, textvariable=entry_var_car, state="readonly").place(x=110,y=140)

    imagen_usuario = Label(win,font=Fuente_3, image=img_usuario,fg="black",text="Limpiar",bg="black").place(x=280,y=20)
    
####Ventana principal ############################

ventana = Tk()
ventana.title("GeodesikApp")
ventana.geometry('566x560')
ventana.config(bg="white")

########## FIJAR VENTANA ##########################
ventana.resizable(0, 0)
backFrame = Frame(master=ventana)
backFrame.pack()
backFrame.propagate(0)
###################################################

# Background
img = PhotoImage(file="D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/im2.png")
etiquetaIcono = Label(ventana,image=img)
etiquetaIcono.pack()
#etiquetaIcono.grid(row=0,column=0)

Fuente_0 = font.Font(family="Bradley Hand ITC", size=30, weight="bold")
Fuente_01 = font.Font(family="Bradley Hand ITC", size=20, weight="bold")
Fuente_02 = font.Font(family="Times New Roman", size=8, weight="bold")
Fuente_1 = font.Font(family="Times New Roman", size=20, weight="bold")
Fuente_2 = font.Font(family="Calibri", size=19, weight="bold")
Fuente_3 = font.Font(family="Times New Roman", size=15, weight="bold")
Fuente_4 = font.Font(family="Times New Roman", size=12, weight="bold")

etiqueta_0 = Label(ventana, font = Fuente_0, text="Geodesi-K", bg= "black", fg="white").place(x=20,y=10)

etiqueta_01 = Label(ventana, font = Fuente_01, text="Ingresar", bg= "black", fg="white").place(x=80,y=80)

etiqueta_1 = Label(ventana, font = Fuente_4, text="ID Usuario: ", bg= "black", fg="white").place(x=100,y=150)

entrada_1 = Entry(ventana, show="*")
entrada_1.place(x=115, y=180)

boton_1 = Button(ventana, text="Ingresar", command=validarUsuario)
boton_1.place(x=150, y=215)

notas = Label(ventana, font = Fuente_02, text="Notas de la aplicación: versión 1.0", bg= "black", fg="white").place(x=20,y=500)

############################################

etiqueta_2 = Label(ventana, font = Fuente_4, text="ID Administrador: ", bg= "black", fg="white").place(x=100,y=300)

entrada_2 = Entry(ventana, show="*")
entrada_2.place(x=115, y=330)

boton_2 = Button(ventana, text="Ingresar", command = validarAdministrador)
boton_2.place(x=150, y=365)

##CARGANDO DATOS PARA PESATAÑA USUARIO#######

B_Limpiar = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/pres.png')
B_Limpiar = B_Limpiar.resize((90, 80), Image.ANTIALIAS)
B_Limpiar = ImageTk.PhotoImage(B_Limpiar)

B_ventas = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/vent.png')
B_ventas = B_ventas.resize((90, 80), Image.ANTIALIAS)
B_ventas = ImageTk.PhotoImage(B_ventas)

img_usuario = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/user.png')
img_usuario = img_usuario.resize((160, 140), Image.ANTIALIAS)
img_usuario = ImageTk.PhotoImage(img_usuario)

entry_var_nom = tk.StringVar()
entry_var_nom.set("Matías Andrés")

entry_var_ape = tk.StringVar()
entry_var_ape.set("Jofré Barraza")

entry_var_rut = tk.IntVar()
entry_var_rut.set(12448798)

entry_var_car = tk.StringVar()
entry_var_car.set("Tester")

#####cargando imagenes y entradas de ventana ventas
img_frec2 = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/frec2.png')
img_frec2 = ImageTk.PhotoImage(img_frec2)

img_frec4 = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/frec4.png')
img_frec4 = ImageTk.PhotoImage(img_frec4)

img_frec6 = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/frec6.png')
img_frec6 = ImageTk.PhotoImage(img_frec6)

img_presupuesto = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/presupuestar.png')
img_presupuesto = img_presupuesto.resize((50, 50), Image.ANTIALIAS)
img_presupuesto = ImageTk.PhotoImage(img_presupuesto)

entry_var_pres = tk.IntVar()
entry_var_pres.set("Presupuesto...")

img_salida = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/salida.png')
img_salida = img_salida.resize((20, 20), Image.ANTIALIAS)
img_salida = ImageTk.PhotoImage(img_salida)

#####cargando imagenes y entradas de ventana Admin
img_barra = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/barra.png')
img_barra = img_barra.resize((100,100), Image.ANTIALIAS)
img_barra = ImageTk.PhotoImage(img_barra)

img_torta = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/torta.png')
img_torta = img_torta.resize((100,100), Image.ANTIALIAS)
img_torta = ImageTk.PhotoImage(img_torta)

img_busqueda = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/busqueda.png')
img_busqueda = img_busqueda.resize((80,80), Image.ANTIALIAS)
img_busqueda = ImageTk.PhotoImage(img_busqueda)

img_actualizar = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/actualizar.png')
img_actualizar = img_actualizar.resize((80,80), Image.ANTIALIAS)
img_actualizar = ImageTk.PhotoImage(img_actualizar)

img_añadir = Image.open('D:/Users/matth/Documents/ICCI/Proyectos/Logo Adomos/botones/añadir.png')
img_añadir = img_añadir.resize((80,80), Image.ANTIALIAS)
img_añadir = ImageTk.PhotoImage(img_añadir)

ventana.mainloop()