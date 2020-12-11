import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font

from PIL import Image, ImageTk

import sqlite3


conn = sqlite3.connect('geodesik.db')
c = conn.cursor()


class Main:

    db_name = 'pruebas.db'

    def __init__(self, window):

        self.wind = window
        self.wind.title('Geodesi-K')
        self.wind.geometry('1600x900')
        self.wind.resizable(0, 0)
        self.wind.config(bg="black")

        fuente_1 = font.Font(family="Bradley Hand ITC",
                             size=25, weight="normal")
        fuente_2 = font.Font(family="Calibri", size=15, weight="normal")

        rec_log = Canvas(self.wind, width=300, height=260)
        rec_log.create_rectangle(0, 0, 350, 350, fill="black", outline="black")
        rec_log.place(x=30, y=30)

        rec_inf = Canvas(self.wind, width=300, height=460)
        rec_inf.create_rectangle(0, 0, 350, 460, fill="black", outline="black")
        rec_inf.place(x=30, y=300)

        rec_dom = Canvas(self.wind, width=605, height=730)
        rec_dom.create_rectangle(
            0, 0, 1220, 730, fill="white", outline="white")
        rec_dom.place(x=340, y=30)

        #Rectangle Cliente

        rec_client = Canvas(self.wind, width=605, height=500)
        rec_client.create_rectangle(
            0, 0, 1220, 730, fill="black", outline="white")
        rec_client.place(x=955, y=30)

        Label(self.wind, font=fuente_2, text="Datos Cliente",
              bg="black", fg="white").place(x=970, y=40)
        Label(self.wind, font=fuente_2, text="Nombre",
              bg="black", fg="white").place(x=970, y=80)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1090, y=80)
        Label(self.wind, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=970, y=120)
        self.entrada_dto_apellido = Entry(self.wind, state=DISABLED)
        self.entrada_dto_apellido.place(x=1090, y=120)
        Label(self.wind, font=fuente_2, text="Correo",
              bg="black", fg="white").place(x=1250, y=80)
        self.entrada_dto_correo = Entry(self.wind, state=DISABLED)
        self.entrada_dto_correo.place(x=1340, y=80)
        Label(self.wind, font=fuente_2, text="Telefono",
              bg="black", fg="white").place(x=1250, y=120)
        self.entrada_dto_telefono = Entry(self.wind, state=DISABLED)
        self.entrada_dto_telefono.place(x=1340, y=120)

        Label(self.wind, font=fuente_2, text="Dirección",
              bg="black", fg="white").place(x=970, y=160)
        Label(self.wind, font=fuente_2, text="Región",
              bg="black", fg="white").place(x=970, y=200)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1090, y=200)
        Label(self.wind, font=fuente_2, text="Comuna",
              bg="black", fg="white").place(x=1250, y=200)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1340, y=200)
        Label(self.wind, font=fuente_2, text="Calle",
              bg="black", fg="white").place(x=970, y=240)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1090, y=240)
        Label(self.wind, font=fuente_2, text="Número",
              bg="black", fg="white").place(x=1250, y=240)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1340, y=240)

        Label(self.wind, font=fuente_2, text="Información de pago y envio",
              bg="black", fg="white").place(x=970, y=280)
        Label(self.wind, font=fuente_2, text="Método de pago",
              bg="black", fg="white").place(x=970, y=320)
        self.entrada_nombre_cliente = Entry(
            self.wind, state=DISABLED, width=48)
        self.entrada_nombre_cliente.place(x=1140, y=320)
        Label(self.wind, font=fuente_2, text="Recibe",
              bg="black", fg="white").place(x=970, y=360)
        Label(self.wind, font=fuente_2, text="Nombre",
              bg="black", fg="white").place(x=970, y=400)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1090, y=400)
        Label(self.wind, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=1250, y=400)
        self.entrada_nombre_cliente = Entry(self.wind, state=DISABLED)
        self.entrada_nombre_cliente.place(x=1340, y=400)
        Label(self.wind, font=fuente_2, text="Rut, DNI o CI",
              bg="black", fg="white").place(x=970, y=440)
        self.entrada_nombre_cliente = Entry(
            self.wind, state=DISABLED, width=48)
        self.entrada_nombre_cliente.place(x=1140, y=440)

        self.boton_ingresar_domo = Button(
            self.wind, text="Aceptar", command=self.generarPresupuesto, state=DISABLED)
        self.boton_ingresar_domo.place(x=1220, y=480)

        # Fin ~ Rectangle Cliente

        # Rectangle Confirmación

        rec_confirmacion = Canvas(self.wind, width=605, height=220)
        rec_confirmacion.create_rectangle(
            0, 0, 1220, 730, fill="black", outline="white")
        rec_confirmacion.place(x=955, y=540)

        Label(self.wind, font=fuente_2, text="Confirmación de Presupuesto",
              bg="black", fg="white").place(x=970, y=550)
        Label(self.wind, font=fuente_2, text="Titular",
              bg="black", fg="white").place(x=970, y=590)
        self.entrada_nombre_cliente = Entry(
            self.wind, state=DISABLED, width=60)
        self.entrada_nombre_cliente.place(x=1090, y=590)

        Label(self.wind, font=fuente_2, text="Recibe",
              bg="black", fg="white").place(x=970, y=630)
        self.entrada_nombre_cliente = Entry(
            self.wind, state=DISABLED, width=60)
        self.entrada_nombre_cliente.place(x=1090, y=630)

        Label(self.wind, font=fuente_2, text="Valor",
              bg="black", fg="white").place(x=970, y=670)
        self.entrada_nombre_cliente = Entry(
            self.wind, state=DISABLED, width=60)
        self.entrada_nombre_cliente.place(x=1090, y=670)

        self.boton_ingresar_domo = Button(
            self.wind, text="Confirmar", command=self.generarPresupuesto, state=DISABLED)
        self.boton_ingresar_domo.place(x=1180, y=720)
        self.boton_ingresar_domo = Button(
            self.wind, text="Eliminar", command=self.generarPresupuesto, state=DISABLED)
        self.boton_ingresar_domo.place(x=1300, y=720)

        # Fin ~ Rectangle Confirmación

        Label(self.wind, font=fuente_1, text="Geodesi-K",
              bg="black", fg="white").place(x=40, y=40)
        Label(self.wind, font=fuente_2, text="Login ",
              bg="black", fg="white").place(x=60, y=80)
        Label(self.wind, font=fuente_2, text="Rut Usuario: ",
              bg="black", fg="white").place(x=100, y=110)

        self.entrada_rut = Entry(self.wind)
        self.entrada_rut.focus()
        self.entrada_rut.place(x=100, y=140)

        Label(self.wind, font=fuente_2, text="Contraseña: ",
              bg="black", fg="white").place(x=100, y=170)

        self.entrada_contraseña = Entry(self.wind, show="*")
        self.entrada_contraseña.place(x=100, y=200)

        self.boton_ingresar = Button(self.wind, text="Ingresar",
                                     command=self.ValidarLogin)
        self.boton_ingresar.place(x=130, y=240)

        Label(self.wind, font=fuente_2, text="Datos de usuario",
              bg="black", fg="white").place(x=40, y=310)
        Label(self.wind, font=fuente_2, text="Nombre",
              bg="black", fg="white").place(x=40, y=350)
        self.entrada_dto_nombre = Entry(self.wind, state=DISABLED)
        self.entrada_dto_nombre.place(x=160, y=350)
        Label(self.wind, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=40, y=390)
        self.entrada_dto_apellido = Entry(self.wind, state=DISABLED)
        self.entrada_dto_apellido.place(x=160, y=390)
        Label(self.wind, font=fuente_2, text="Correo",
              bg="black", fg="white").place(x=40, y=430)
        self.entrada_dto_correo = Entry(self.wind, state=DISABLED)
        self.entrada_dto_correo.place(x=160, y=430)
        Label(self.wind, font=fuente_2, text="Telefono",
              bg="black", fg="white").place(x=40, y=470)
        self.entrada_dto_telefono = Entry(self.wind, state=DISABLED)
        self.entrada_dto_telefono.place(x=160, y=470)

        self.boton_ingresar_domo = Button(
            self.wind, text="Ingresar nuevo presupuesto", command=self.generarPresupuesto, state=DISABLED)
        self.boton_ingresar_domo.place(x=75, y=510)

        #Agregando imágenes
        self.img_frec2 = Image.open('./imagenes/frec2.png')
        self.img_frec2 = ImageTk.PhotoImage(self.img_frec2)

        self.img_frec4 = Image.open('./imagenes/frec4.png')
        self.img_frec4 = ImageTk.PhotoImage(self.img_frec4)

        self.img_frec6 = Image.open('./imagenes/frec6.png')
        self.img_frec6 = ImageTk.PhotoImage(self.img_frec6)

        Label(self.wind, font=fuente_2, text="Seleccionar Caracteristicas ",
              bg="white", fg="black").place(x=380, y=50)

        # Label(self.wind, font=fuente_2, text="ID",
        #       bg="white", fg="black").place(x=450, y=50)

        self.domo_id = Entry(self.wind, width=2, state=DISABLED)
        self.domo_id.place(x=910, y=40)

        Label(self.wind, image=self.img_frec2, fg="black",
              text="Limpiar", bg="white").place(x=380, y=103)
        Label(self.wind, image=self.img_frec4, fg="black",
              text="Limpiar", bg="white").place(x=560, y=110)
        Label(self.wind, image=self.img_frec6, fg="black",
              text="Limpiar", bg="white").place(x=750, y=110)

        # Table
        columns = ("#1", "#2,", "#3,", "#4,", "5,")
        self.tree = ttk.Treeview(
            self.wind, show='headings', height=5, columns=columns)
        self.tree.place(x=380, y=363)
        self.tree.column("#1", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#2", width=115, minwidth=100, stretch=tk.NO)
        self.tree.column("#3", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#4", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#5", width=100, minwidth=100, stretch=tk.NO)
        self.tree.heading('#1', text='Material ID', anchor=tk.CENTER)
        self.tree.heading('#2', text='Nombre', anchor=tk.CENTER)
        self.tree.heading('#3', text='Tipo', anchor=tk.CENTER)
        self.tree.heading('#4', text='Cantidad', anchor=tk.CENTER)
        self.tree.heading('#5', text='Valor', anchor=tk.CENTER)

        self.radioFrecuencia = IntVar()
        self.frec1 = Radiobutton(self.wind, text='Frecuencia 2', variable=self.radioFrecuencia,
                                 value=350000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec2 = Radiobutton(self.wind, text='Frecuencia 4', variable=self.radioFrecuencia,
                                 value=700000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec3 = Radiobutton(self.wind, text='Frecuencia 6', variable=self.radioFrecuencia,
                                 value=1000000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec1.place(x=380, y=210)
        self.frec2.place(x=560, y=210)
        self.frec3.place(x=750, y=210)

        self.radioDiametro = IntVar()
        self.diam1 = Radiobutton(self.wind, text='5 metros', variable=self.radioDiametro,
                                 value=5, bg="white", command=self.mostrarDiametro, padx=34, pady=10, state=DISABLED)
        self.diam2 = Radiobutton(self.wind, text='10 metros', variable=self.radioDiametro,
                                 value=10, bg="white", command=self.mostrarDiametro, padx=30, pady=10, state=DISABLED)
        self.diam3 = Radiobutton(self.wind, text='15 metros', variable=self.radioDiametro,
                                 value=15, bg="white", command=self.mostrarDiametro, padx=30, pady=10, state=DISABLED)
        self.diam1.place(x=380, y=260)
        self.diam2.place(x=560, y=260)
        self.diam3.place(x=750, y=260)

        self.radioTipo = StringVar()
        self.tipo1 = Radiobutton(self.wind, text='Habitacional', variable=self.radioTipo,
                                 value="habitacional", bg="white", command=self.mostrarTipo, padx=20, pady=10, state=DISABLED)
        self.tipo2 = Radiobutton(self.wind, text='Invernadero', variable=self.radioTipo,
                                 value="invernadero", bg="white", command=self.mostrarTipo, padx=23, pady=10, state=DISABLED)
        self.tipo3 = Radiobutton(self.wind, text='Exposición', variable=self.radioTipo,
                                 value="exposicion", bg="white", command=self.mostrarTipo, padx=27, pady=10, state=DISABLED)
        self.tipo1.place(x=380, y=310)
        self.tipo2.place(x=560, y=310)
        self.tipo3.place(x=750, y=310)

        self.boton_agregar_domo = Button(
            self.wind, text="Ingresar Domo", command=self.AgregarDomo, state=DISABLED)
        self.boton_agregar_domo.place(x=500, y=510)

    def mostrarFrecuencia(self):
        print(self.radioFrecuencia.get())

    def mostrarDiametro(self):
        print(self.radioDiametro.get())

    def mostrarTipo(self):
        print(self.radioTipo.get())

    def ValidarLogin(self):
        print(c.execute("select rut, nombre, apellido, correo, telefono from usuario where rut = ? and contraseña = ?",
                        (self.entrada_rut.get(), self.entrada_contraseña.get())))
        data = c.fetchall()
        # ewe = tuple(data)
        # print(type(data))
        if data:
            for row in data:
                row
            #self.radioLeido1.config(state = NORMAL)
            self.entrada_dto_nombre.config(
                textvariable=StringVar(self.wind, value=row[1]))
            self.entrada_dto_apellido.config(
                textvariable=StringVar(self.wind, value=row[2]))
            self.entrada_dto_correo.config(
                textvariable=StringVar(self.wind, value=row[3]))
            self.entrada_dto_telefono.config(
                textvariable=StringVar(self.wind, value=row[4]))
            self.boton_ingresar_domo.config(state=NORMAL)
            print('no esta vacia')
            #print(row[(0)])
            self.entrada_rut.delete(0, END)
            self.entrada_contraseña.delete(0, END)
            return True
        else:
            print('esta vacia')
            return False

    def get_materiales(self):
        #Limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        db_rows = c.execute(
            'SELECT * FROM materiales ORDER BY id_material DESC')
        #rellenando datos
        for row in db_rows:
            self.tree.insert('', 0, values=(
                row[0], row[1], row[2], row[3], row[4]))
            #print(row)

    def generarPresupuesto(self):
        self.boton_ingresar_domo.config(state=DISABLED)
        self.frec1.config(state=NORMAL)
        self.frec2.config(state=NORMAL)
        self.frec3.config(state=NORMAL)
        self.diam1.config(state=NORMAL)
        self.diam2.config(state=NORMAL)
        self.diam3.config(state=NORMAL)
        self.tipo1.config(state=NORMAL)
        self.tipo2.config(state=NORMAL)
        self.tipo3.config(state=NORMAL)
        self.boton_agregar_domo.config(state=NORMAL)
        self.get_materiales()
        c.execute(
            "insert into domo (frecuencia, metros, tipo) values (1, 2, 'asd')")
        c.execute('select id_domo from domo')
        data = c.fetchall()
        if data:
            for row in data:
                print(row)
        self.domo_id.config(textvariable=StringVar(self.wind, value=row[0]))

    def AgregarDomo(self):
        print(self.radioFrecuencia.get())
        print(self.radioDiametro.get())
        print(self.radioTipo.get())
        c.execute('update domo set frecuencia = ?, metros = ?, tipo = ? where id_domo = 2',
                  (self.radioFrecuencia.get(), self.radioDiametro.get(), self.radioTipo.get()))
        conn.commit()


if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()
