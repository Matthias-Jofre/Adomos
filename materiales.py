from tkinter import ttk
from tkinter import *
from tkinter import font

from PIL import Image,ImageTk

import sqlite3

db_name = 'database.db'

def run_query(self, query, parameters = ()):
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

def get_usuario(rut, contraseña):
    
    def mostrarFrecuencia():
        print(radioLeido.get())
    
    rec_dom = Canvas(ventana, width=1000, height=650)
    rec_dom.create_rectangle(0, 0, 1000, 650, fill="white", outline = "white")
    rec_dom.place(x = 500, y = 60)
    #rec_dom.destroy()
    radioLeido = IntVar() 
    frec1 = Radiobutton(ventana,text='Frecuencia 2',variable=radioLeido, value=350000, bg="white", command=mostrarFrecuencia) 
    frec2 = Radiobutton(ventana,text='Frecuencia 4',variable=radioLeido, value=700000, bg="white", command=mostrarFrecuencia) 
    frec3 = Radiobutton(ventana,text='Frecuencia 6',variable=radioLeido, value=1000000, bg="white", command=mostrarFrecuencia) 
    frec1.place(x=667,y=270)
    frec2.place(x=945,y=270)
    frec3.place(x=1218,y=270)    
    Label(ventana,font=Fuente_3, image=img_frec2,fg="black",text="Limpiar",bg="white").place(x=650,y=163)
    Label(ventana,font=Fuente_3, image=img_frec4,fg="black",text="Limpiar",bg="white").place(x=925,y=170)
    Label(ventana,font=Fuente_3, image=img_frec6,fg="black",text="Limpiar",bg="white").place(x=1200,y=170)
    radioLeido = IntVar() 
    frec1 = Radiobutton(ventana,text='Frecuencia 2',variable=radioLeido, value=350000, bg="white", command=mostrarFrecuencia) 
    frec2 = Radiobutton(ventana,text='Frecuencia 4',variable=radioLeido, value=700000, bg="white", command=mostrarFrecuencia) 
    frec3 = Radiobutton(ventana,text='Frecuencia 6',variable=radioLeido, value=1000000, bg="white", command=mostrarFrecuencia) 
    frec1.place(x=667,y=270)
    frec2.place(x=945,y=270)
    frec3.place(x=1218,y=270)

    # query = 'SELECT rut FROM usuario_p WHERE rut = ? AND contraseña = ?'
    # parametros = (rut, contraseña)
    # run_query(query, parametros)
    # entrada_1.delete(0, END)
    # entrada_2.delete(0, END)

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

#####cargando imagenes y entradas de ventana ventas
img_frec2 = Image.open('./imagenes/frec2.png')
img_frec2 = ImageTk.PhotoImage(img_frec2)

img_frec4 = Image.open('./imagenes/frec4.png')
img_frec4 = ImageTk.PhotoImage(img_frec4)

img_frec6 = Image.open('./imagenes/frec6.png')
img_frec6 = ImageTk.PhotoImage(img_frec6)
 
ventana.mainloop()