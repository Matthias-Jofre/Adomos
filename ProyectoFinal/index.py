import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font

from PIL import Image, ImageTk

import sqlite3

from datetime import date
from datetime import datetime

conn = sqlite3.connect('geodesik.db')
c = conn.cursor()


class Main:

    db_name = 'pruebas.db'

    def __init__(self, window):

        self.wind = window
        self.wind.title('Geodesi-K')
        self.wind.geometry('980x800')
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

        # # Rectangle Confirmación

        # rec_confirmacion = Canvas(self.wind, width=605, height=220)
        # rec_confirmacion.create_rectangle(
        #     0, 0, 1220, 730, fill="black", outline="white")
        # rec_confirmacion.place(x=955, y=540)

        # Label(self.wind, font=fuente_2, text="Confirmación de Presupuesto",
        #       bg="black", fg="white").place(x=970, y=550)
        # Label(self.wind, font=fuente_2, text="Titular",
        #       bg="black", fg="white").place(x=970, y=590)
        # self.entrada_nombre_cliente = Entry(
        #     self.wind, state=DISABLED, width=60)
        # self.entrada_nombre_cliente.place(x=1090, y=590)

        # Label(self.wind, font=fuente_2, text="Recibe",
        #       bg="black", fg="white").place(x=970, y=630)
        # self.entrada_nombre_cliente = Entry(
        #     self.wind, state=DISABLED, width=60)
        # self.entrada_nombre_cliente.place(x=1090, y=630)

        # Label(self.wind, font=fuente_2, text="Valor",
        #       bg="black", fg="white").place(x=970, y=670)
        # self.entrada_nombre_cliente = Entry(
        #     self.wind, state=DISABLED, width=60)
        # self.entrada_nombre_cliente.place(x=1090, y=670)

        # self.boton_ingresar_domo = Button(
        #     self.wind, text="Confirmar", command=self.generarPresupuesto, state=DISABLED)
        # self.boton_ingresar_domo.place(x=1180, y=720)
        # self.boton_ingresar_domo = Button(
        #     self.wind, text="Eliminar", command=self.generarPresupuesto, state=DISABLED)
        # self.boton_ingresar_domo.place(x=1300, y=720)

        # # Fin ~ Rectangle Confirmación

        # Login Usuario

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
        self.entrada_dto_nombre = Entry(self.wind, state='readonly')
        self.entrada_dto_nombre.place(x=160, y=350)
        Label(self.wind, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=40, y=390)
        self.entrada_dto_apellido = Entry(self.wind, state='readonly')
        self.entrada_dto_apellido.place(x=160, y=390)
        Label(self.wind, font=fuente_2, text="Correo",
              bg="black", fg="white").place(x=40, y=430)
        self.entrada_dto_correo = Entry(self.wind, state='readonly')
        self.entrada_dto_correo.place(x=160, y=430)
        Label(self.wind, font=fuente_2, text="Telefono",
              bg="black", fg="white").place(x=40, y=470)
        self.entrada_dto_telefono = Entry(self.wind, state='readonly')
        self.entrada_dto_telefono.place(x=160, y=470)

        # self.boton_ingresar_domo = Button(
        #     self.wind, text="Ingresar nuevo presupuesto", command=self.generarPresupuesto, state=DISABLED)
        # self.boton_ingresar_domo.place(x=75, y=510)

        # Fin ~ Login Usuario

        # Presupuesto de domo

        Label(self.wind, font=fuente_2, text="ID Presupuesto:",
              bg="white", fg="black").place(x=345, y=35)
        self.domo_id = Entry(self.wind, state='readonly')
        self.domo_id.place(x=485, y=42)
        Label(self.wind, font=fuente_2, text="Fecha:",
              bg="white", fg="black").place(x=620, y=35)
        self.domo_fecha = Entry(self.wind, state='readonly', width = 10)
        self.domo_fecha.place(x=690, y=42)
   
        Label(self.wind, font=fuente_2, text="Rut Cliente",
              bg="white", fg="black").place(x=345, y=75)
        self.cliente_rut = Entry(self.wind, state='readonly')
        self.cliente_rut.place(x=485, y=80)        
        Label(self.wind, font=fuente_2, text="Nombre",
              bg="white", fg="black").place(x=345, y=115)
        self.cliente_nombre = Entry(self.wind, state = 'readonly')
        self.cliente_nombre.place(x=485, y=120)                 
        Label(self.wind, font=fuente_2, text="Apellido",
              bg="white", fg="black").place(x=620, y=115)  
        self.cliente_apellido = Entry(self.wind, state = 'readonly')
        self.cliente_apellido.place(x=740, y=120)                 
        Label(self.wind, font=fuente_2, text="Rut",
              bg="white", fg="black").place(x=345, y=155)
        self.cliente_rutb = Entry(self.wind, state = 'readonly')
        self.cliente_rutb.place(x=485, y=160)                 
        Label(self.wind, font=fuente_2, text="Telefono",
              bg="white", fg="black").place(x=620, y=155)                
        self.cliente_telefono = Entry(self.wind, state = 'readonly')
        self.cliente_telefono.place(x=740, y=160)                 


        self.b_mas = Image.open('./imagenes/mas.png')
        self.b_mas = self.b_mas.resize((20, 20), Image.ANTIALIAS)
        self.b_mas = ImageTk.PhotoImage(self.b_mas) 
        self.b_buscar = Image.open('./imagenes/lupa.png')
        self.b_buscar = self.b_buscar.resize((20, 20), Image.ANTIALIAS)
        self.b_buscar = ImageTk.PhotoImage(self.b_buscar) 
        self.b_actualizar = Image.open('./imagenes/refrescar.png')
        self.b_actualizar = self.b_actualizar.resize((20, 20), Image.ANTIALIAS)
        self.b_actualizar = ImageTk.PhotoImage(self.b_actualizar)
        self.boton_mas = Button(self.wind, font=fuente_2, image=self.b_mas, fg="black",text="Limpiar", command = self.ingresarCliente)
        self.boton_mas.place(x=650, y=80)
        self.boton_buscar = Button(self.wind, font=fuente_2, image=self.b_buscar, fg="black",text="Limpiar", command = self.buscarCliente)
        self.boton_buscar.place(x=620, y=80)
        self.boton_actualizar = Button(self.wind, font=fuente_2, image=self.b_actualizar, fg="black",text="Limpiar", command = self.sumarValores)
        self.boton_actualizar.place(x=773, y=644)

        # Botones Usuario
        self.b_domo = Image.open('./imagenes/domo.png')
        self.b_domo = self.b_domo.resize((90, 90), Image.ANTIALIAS)
        self.b_domo = ImageTk.PhotoImage(self.b_domo)
        self.boton_domo = Button(self.wind, font=fuente_2, image=self.b_domo, fg="white",text="Limpiar", bg = "white", command=self.generarPresupuesto, state=DISABLED)
        self.boton_domo.place(x=80, y=520)        
        self.b_herramientas = Image.open('./imagenes/herramientas.png')
        self.b_herramientas = self.b_herramientas.resize((90, 90), Image.ANTIALIAS)
        self.b_herramientas = ImageTk.PhotoImage(self.b_herramientas)
        self.boton_herramientas = Button(self.wind, font=fuente_2, image=self.b_herramientas, fg="white",text="Limpiar", bg = "white", command = self.BotonAgregarMaterial, state=DISABLED)
        self.boton_herramientas.place(x=190, y=520)        
        self.b_estadisticas = Image.open('./imagenes/estadistica.png')
        self.b_estadisticas = self.b_estadisticas.resize((90, 90), Image.ANTIALIAS)
        self.b_estadisticas = ImageTk.PhotoImage(self.b_estadisticas)
        self.boton_estadisticas = Button(self.wind, font=fuente_2, image=self.b_estadisticas, fg="white",text="Limpiar", bg = "white", state=DISABLED)
        self.boton_estadisticas.place(x=80, y=630)        
        self.b_editar = Image.open('./imagenes/formulario.png')
        self.b_editar = self.b_editar.resize((90, 90), Image.ANTIALIAS)
        self.b_editar = ImageTk.PhotoImage(self.b_editar)
        self.boton_editar = Button(self.wind, font=fuente_2, image=self.b_editar, fg="white",text="Limpiar", bg = "white", state=DISABLED)
        self.boton_editar.place(x=190, y=630)                     
        # Fin ~ Botones Usuario

        # #Agregando imágenes
        self.img_frec2 = Image.open('./imagenes/frec2.png')
        self.img_frec2 = ImageTk.PhotoImage(self.img_frec2)

        self.img_frec4 = Image.open('./imagenes/frec4.png')
        self.img_frec4 = ImageTk.PhotoImage(self.img_frec4)

        self.img_frec6 = Image.open('./imagenes/frec6.png')
        self.img_frec6 = ImageTk.PhotoImage(self.img_frec6)

        # Label(self.wind, font=fuente_2, text="Seleccionar Caracteristicas ",
        #       bg="white", fg="black").place(x=345, y=190)

        Label(self.wind, image=self.img_frec2, fg="black",
              text="Limpiar", bg="white").place(x=360, y=220)
        Label(self.wind, image=self.img_frec4, fg="black",
              text="Limpiar", bg="white").place(x=560, y=227)
        Label(self.wind, image=self.img_frec6, fg="black",
              text="Limpiar", bg="white").place(x=770, y=231)

        self.radioFrecuencia = IntVar()
        self.frec1 = Radiobutton(self.wind, text='Frecuencia 2', variable=self.radioFrecuencia,
                                 value=350000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec2 = Radiobutton(self.wind, text='Frecuencia 4', variable=self.radioFrecuencia,
                                 value=700000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec3 = Radiobutton(self.wind, text='Frecuencia 6', variable=self.radioFrecuencia,
                                 value=1000000, bg="white", command=self.mostrarFrecuencia, padx=20, pady=10, state=DISABLED)
        self.frec1.place(x=360, y=310)
        self.frec2.place(x=560, y=310)
        self.frec3.place(x=760, y=310)

        self.radioDiametro = IntVar()
        self.diam1 = Radiobutton(self.wind, text='5 metros', variable=self.radioDiametro,
                                 value=5, bg="white", command=self.mostrarDiametro, padx=34, pady=10, state=DISABLED)
        self.diam2 = Radiobutton(self.wind, text='10 metros', variable=self.radioDiametro,
                                 value=10, bg="white", command=self.mostrarDiametro, padx=30, pady=10, state=DISABLED)
        self.diam3 = Radiobutton(self.wind, text='15 metros', variable=self.radioDiametro,
                                 value=15, bg="white", command=self.mostrarDiametro, padx=30, pady=10, state=DISABLED)
        self.diam1.place(x=347, y=360)
        self.diam2.place(x=550, y=360)
        self.diam3.place(x=750, y=360)

        self.radioTipo = StringVar()
        self.tipo1 = Radiobutton(self.wind, text='Habitacional', variable=self.radioTipo,
                                 value="habitacional", bg="white", command=self.mostrarTipo, padx=20, pady=10, state=DISABLED)
        self.tipo2 = Radiobutton(self.wind, text='Invernadero', variable=self.radioTipo,
                                 value="invernadero", bg="white", command=self.mostrarTipo, padx=23, pady=10, state=DISABLED)
        self.tipo3 = Radiobutton(self.wind, text='Exposición', variable=self.radioTipo,
                                 value="exposicion", bg="white", command=self.mostrarTipo, padx=27, pady=10, state=DISABLED)
        self.tipo1.place(x=360 , y=410)
        self.tipo2.place(x=560, y=410)
        self.tipo3.place(x=753, y=410)

        # Table
        columns = ("#1", "#2,", "#3,", "#4,", "5,")
        self.tree = ttk.Treeview(
            self.wind, show='headings', height=5, columns=columns)
        self.tree.place(x=380, y=470)
        self.tree.column("#1", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#2", width=115, minwidth=100, stretch=tk.NO)
        self.tree.column("#3", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#4", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("#5", width=100, minwidth=100, stretch=tk.NO)
        self.tree.heading('#1', text='ID Material', anchor=tk.CENTER)
        self.tree.heading('#2', text='Nombre', anchor=tk.CENTER)
        self.tree.heading('#3', text='Tipo', anchor=tk.CENTER)
        self.tree.heading('#4', text='Cantidad', anchor=tk.CENTER)
        self.tree.heading('#5', text='Valor', anchor=tk.CENTER)

        Button(self.wind, text="Agregar material", state=NORMAL, command = self.ventanaAgregarMaterialDomo).place(x=379, y=597, width = 260, height = 25)
        Button(self.wind, text="Borrar material", state=NORMAL).place(x=638, y=597, width = 260, height = 25)

        self.boton_agregar_domo = Button(
            self.wind, text="Ingresar Domo", command=self.AgregarDomo, state=DISABLED)
        self.boton_agregar_domo.place(x=500, y=700)

        Label(self.wind, font=fuente_2, text="Presupuesto: ",
              bg="white", fg="black").place(x=450, y=640)    
        self.cliente_presupuesto = Entry(self.wind, state = 'readonly')
        self.cliente_presupuesto.place(x=570, y=645, width = 200, height = 25)                          
        # Fin ~ Presupuesto de domo

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
            self.boton_domo.config(state=NORMAL)
            self.boton_herramientas.config(state=NORMAL)
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
            'SELECT * FROM material ORDER BY id_material DESC')
        #rellenando datos
        for row in db_rows:
            self.tree.insert('', 0, values=(
                row[0], row[1], row[2], row[3]))
            #print(row)

    def generarPresupuesto(self):
        self.boton_domo.config(state=DISABLED)
        self.cliente_rut.config(state=NORMAL)
        self.get_materiales()
        c.execute(
            "insert into domo (frecuencia, metros, tipo) values (1, 2, 'asd')")
        c.execute('select id_domo from domo')
        conn.commit()
        data = c.fetchall()
        if data:
            for row in data:
                print(row)
        self.domo_id.config(textvariable=StringVar(self.wind, value=row[0]))
        self.domo_fecha.config(textvariable=StringVar(self.wind, value=date.today()))

    def AgregarDomo(self):
        print(self.radioFrecuencia.get())
        print(self.radioDiametro.get())
        print(self.radioTipo.get())
        c.execute('update domo set frecuencia = ?, metros = ?, tipo = ? where id_domo = ?',
                  (self.radioFrecuencia.get(), self.radioDiametro.get(), self.radioTipo.get(), self.domo_id.get()))
        conn.commit()

    def ingresarCliente(self):
        fuente_2 = font.Font(family="Calibri", size=15, weight="normal")
        self.wind_usuario = Toplevel()
        self.wind_usuario.geometry('520x500')
        self.wind_usuario.resizable(0, 0)
        self.wind_usuario.config(bg="black")
        self.wind_usuario.title('Agregar usuario')

        Label(self.wind_usuario, font=fuente_2, text="Datos Cliente",
              bg="black", fg="white").place(x=10, y=10)
        Label(self.wind_usuario, font=fuente_2, text="Nombre",
              bg="black", fg="white").place(x=10, y=50)
        self.entrada_cliente_nombre = Entry(self.wind_usuario)
        self.entrada_cliente_nombre.place(x=130, y=55)
        Label(self.wind_usuario, font=fuente_2, text="Rut",
              bg="black", fg="white").place(x=10, y=90)
        self.entrada_cliente_rut = Entry(self.wind_usuario)
        self.entrada_cliente_rut.place(x=130, y=95)
        Label(self.wind_usuario, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=290, y=50)
        self.entrada_cliente_apellido = Entry(self.wind_usuario)
        self.entrada_cliente_apellido.place(x=380, y=55)
        Label(self.wind_usuario, font=fuente_2, text="Telefono",
              bg="black", fg="white").place(x=290, y=90)
        self.entrada_cliente_telefono = Entry(self.wind_usuario)
        self.entrada_cliente_telefono.place(x=380, y=95)

        Label(self.wind_usuario, font=fuente_2, text="Dirección",
              bg="black", fg="white").place(x=10, y=130)
        Label(self.wind_usuario, font=fuente_2, text="Región",
              bg="black", fg="white").place(x=10, y=170)
        self.entrada_cliente_region = Entry(self.wind_usuario)
        self.entrada_cliente_region.place(x=130, y=175)
        Label(self.wind_usuario, font=fuente_2, text="Comuna",
              bg="black", fg="white").place(x=290, y=170)
        self.entrada_cliente_comuna = Entry(self.wind_usuario)
        self.entrada_cliente_comuna.place(x=380, y=175)
        Label(self.wind_usuario, font=fuente_2, text="Calle",
              bg="black", fg="white").place(x=10, y=210)
        self.entrada_cliente_calle = Entry(self.wind_usuario)
        self.entrada_cliente_calle.place(x=130, y=215)
        Label(self.wind_usuario, font=fuente_2, text="Número",
              bg="black", fg="white").place(x=290, y=210)
        self.entrada_cliente_numero = Entry(self.wind_usuario)
        self.entrada_cliente_numero.place(x=380, y=215)

        Label(self.wind_usuario, font=fuente_2, text="Información de pago y envio",
              bg="black", fg="white").place(x=10, y=250)
        Label(self.wind_usuario, font=fuente_2, text="Método de pago",
              bg="black", fg="white").place(x=10, y=290)
        self.entrada_cliente_pago = Entry(
            self.wind_usuario, width=53)
        self.entrada_cliente_pago.place(x=180, y=295)
        Label(self.wind_usuario, font=fuente_2, text="Datos de receptor",
              bg="black", fg="white").place(x=10, y=330)
        Label(self.wind_usuario, font=fuente_2, text="Nombre",
              bg="black", fg="white").place(x=10, y=370)
        self.entrada_clienteRec_nombre = Entry(self.wind_usuario)
        self.entrada_clienteRec_nombre.place(x=130, y=375)
        Label(self.wind_usuario, font=fuente_2, text="Apellido",
              bg="black", fg="white").place(x=290, y=370)
        self.entrada_clienteRec_apellido = Entry(self.wind_usuario)
        self.entrada_clienteRec_apellido.place(x=380, y=375)
        Label(self.wind_usuario, font=fuente_2, text="Rut / DNI / CI ",
              bg="black", fg="white").place(x=10, y=410)
        self.entrada_clienteRec_rut = Entry(
            self.wind_usuario, width=53)
        self.entrada_clienteRec_rut.place(x=180, y=415)

        self.botono_ingresar_cliente = Button(
            self.wind_usuario, text="Añadir cliente", command=self.agregarCliente)
        self.botono_ingresar_cliente.place(x=215, y=450)
        self.wind_usuario.mainloop()

    def agregarCliente(self):
        print(self.entrada_cliente_nombre.get())
        c.execute('insert into cliente values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.entrada_cliente_nombre.get(
        ), self.entrada_cliente_apellido.get(), self.entrada_cliente_rut.get(), self.entrada_cliente_telefono.get(), self.entrada_cliente_region.get(), self.entrada_cliente_comuna.get(), self.entrada_cliente_calle.get(), self.entrada_cliente_numero.get(), self.entrada_cliente_pago.get(), self.entrada_clienteRec_nombre.get(), self.entrada_clienteRec_apellido.get(), self.entrada_clienteRec_rut.get()))
        conn.commit()
        self.wind_usuario.destroy()

    def buscarCliente(self):
        print(self.cliente_rut.get())
        print(c.execute("SELECT nombre, apellido, rut, telefono from cliente where rut = ?",
                        (self.cliente_rut.get(),)))        
        data = c.fetchall()
        if data:
            for row in data:
                row
            #self.radioLeido1.config(state = NORMAL)
            self.cliente_nombre.config(
                textvariable=StringVar(self.wind, value=row[0]))
            self.cliente_apellido.config(
                textvariable=StringVar(self.wind, value=row[1]))
            self.cliente_rutb.config(
                textvariable=StringVar(self.wind, value=row[2]))
            self.cliente_telefono.config(
                textvariable=StringVar(self.wind, value=row[3]))
            #self.boton_ingresar_domo.config(state=NORMAL)
            print('no esta vacia')
            self.cliente_rut.delete(0, END)
            #print(row[(0)])
            #self.entrada_rut.delete(0, END)
            #self.entrada_contraseña.delete(0, END)
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
            return True
        else:
            print('esta vacia')
            return False

    def sumarValores(self):
        self.cliente_presupuesto.config(
            textvariable=StringVar(self.wind, self.radioDiametro.get()*self.radioFrecuencia.get()))        

    def BotonAgregarMaterial(self):
        self.wind_material = Toplevel()
        self.wind_material.resizable(0, 0)
        self.wind_material.config(bg="white")

        # Creando contenedor
        frame = LabelFrame(self.wind_material, text = 'Registrar un nuevo material', bg = "white")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Entrada de nombre 
        Label(frame, text = 'Nombre: ', bg = "white").grid(row = 1, column = 0)
        self.material_nombre = Entry(frame)
        self.material_nombre.focus()
        self.material_nombre.grid(row = 1, column = 1)

        # Entrada de tipo
        Label(frame, text = 'Tipo: ', bg = "white").grid(row = 2, column = 0)
        self.material_tipo = Entry(frame)
        self.material_tipo.grid(row = 2, column = 1)

        # precio Input
        Label(frame, text = 'Precio: ', bg = "white").grid(row = 4, column = 0)
        self.material_precio = Entry(frame)
        self.material_precio.grid(row = 4, column = 1)

        # Button Add Product
        ttk.Button(frame, text='Agergar material', command = self.agregarMaterial).grid(
            row=5, columnspan=2, sticky=W + E)

        # Tabla
        columnas = ("#1", "#2,", "#3,", "#4,")
        self.tabla_materiales = ttk.Treeview(
            self.wind_material, show='headings', height=5, columns=columnas)
        self.tabla_materiales.grid(row=4, column=0, columnspan=2)
        self.tabla_materiales.heading('#1', text='ID', anchor=CENTER)
        self.tabla_materiales.heading('#2', text='Nombre', anchor=CENTER)
        self.tabla_materiales.heading('#3', text='Tipo', anchor=CENTER)
        self.tabla_materiales.heading('#4', text='Precio', anchor=CENTER)
        # Buttons
        ttk.Button(self.wind_material, text = 'Borrar', command = self.borrarMaterial).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(self.wind_material, text = 'Editar', command = self.BotonEditarMaterial).grid(row = 5, column = 1, sticky = W + E)
        
        self.getMateriales()

    def getMateriales(self):
        records = self.tabla_materiales.get_children()
        for element in records:
            self.tabla_materiales.delete(element)
        c.execute('select * from materiales order by id_material desc')    
        data = c.fetchall()
        for row in data:
            self.tabla_materiales.insert('', 0, text=row[0], values=(row[0], row[1], row[2], row[3]))

    def agregarMaterial(self):
            c.execute('INSERT INTO materiales VALUES(NULL, ?, ?, ?)', (self.material_nombre.get(), self.material_tipo.get(),self.material_precio.get()))
            conn.commit()
            self.material_nombre.delete(0, END)
            self.material_tipo.delete(0, END)
            self.material_precio.delete(0, END)    
            self.getMateriales()    

    def borrarMaterial(self):
        self.tabla_materiales.item(self.tabla_materiales.selection())['values'][0]
        self.id_material = self.tabla_materiales.item(self.tabla_materiales.selection())['text']
        print(self.id_material)
        c.execute('DELETE FROM materiales WHERE id_material = ?', (self.id_material, ))
        conn.commit()
        self.getMateriales()            

    def BotonEditarMaterial(self):
        self.tabla_materiales.item(self.tabla_materiales.selection())['values'][0]
        old_material_nombre = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][1]
        old_material_tipo = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][2]
        old_material_precio = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][3]

        self.edit_wind_material = Toplevel()
        self.edit_wind_material.geometry('300x160')
        self.edit_wind_material.resizable(0, 0)
        self.edit_wind_material.config(bg="white")
        self.edit_wind_material.title = "Editar material"

        #Old nombre
        Label(self.edit_wind_material, text = "Nombre anterior", bg="white").grid(row = 0, column = 1)
        Entry(self.edit_wind_material, textvariable = StringVar(self.edit_wind_material, value = old_material_nombre), state = 'readonly').grid(row = 0, column = 2)
        
        #New nombre
        Label(self.edit_wind_material, text = "Nombre nuevo", bg="white").grid(row = 1, column = 1)
        new_material_nombre = Entry(self.edit_wind_material)
        new_material_nombre.grid(row = 1, column = 2)

        #Old tipo
        Label(self.edit_wind_material, text = "Tipo anterior", bg="white").grid(row = 2, column = 1)
        Entry(self.edit_wind_material, textvariable = StringVar(self.edit_wind_material, value = old_material_tipo), state = 'readonly').grid(row = 2, column = 2)
        #New tipo
        Label(self.edit_wind_material, text = "Tipo nuevo", bg="white").grid(row = 3, column = 1)
        new_material_tipo = Entry(self.edit_wind_material)
        new_material_tipo.grid(row = 3, column = 2)

        #Old precio
        Label(self.edit_wind_material, text = "Precio anterior", bg="white").grid(row = 4, column = 1)
        Entry(self.edit_wind_material, textvariable = StringVar(self.edit_wind_material, value = old_material_precio), state = 'readonly').grid(row = 4, column = 2)
        #New precio
        Label(self.edit_wind_material, text = "Precio nuevo", bg="white").grid(row = 5, column = 1)
        new_material_precio = Entry(self.edit_wind_material)
        new_material_precio.grid(row = 5, column = 2)

        Button(self.edit_wind_material, text = 'Actualizar', command = lambda: self.editarMaterial(new_material_nombre.get(), old_material_nombre, new_material_tipo.get(),old_material_tipo, new_material_precio.get(), old_material_precio)).grid(row=8, column=2, sticky = W + E)

    def editarMaterial(self, new_material_nombre, old_material_nombre, new_material_tipo, old_material_tipo, new_material_precio, old_material_precio):
        c.execute('UPDATE materiales SET nombre = ?, tipo = ?, precio = ? WHERE nombre = ? AND tipo = ? AND precio = ?', (new_material_nombre, new_material_tipo, new_material_precio, old_material_nombre, old_material_tipo, old_material_precio))
        conn.commit()
        self.edit_wind_material.destroy()
        self.getMateriales()

    def ventanaAgregarMaterialDomo(self):
        self.wind_material_domo = Toplevel()
        self.wind_material_domo.geometry('802x152')
        self.wind_material_domo.resizable(0, 0)
        self.wind_material_domo.config(bg="white")
        
        columnas = ("#1", "#2,", "#3,", "#4,")
        self.tabla_materiales = ttk.Treeview(
            self.wind_material_domo, show='headings', height=5, columns=columnas)
        self.tabla_materiales.grid(row=4, column=0, columnspan=2)
        self.tabla_materiales.heading('#1', text='ID', anchor=CENTER)
        self.tabla_materiales.heading('#2', text='Nombre', anchor=CENTER)
        self.tabla_materiales.heading('#3', text='Tipo', anchor=CENTER)
        self.tabla_materiales.heading('#4', text='Precio', anchor=CENTER)
        
        ttk.Button(self.wind_material_domo, text = 'Agregar', command = self.agregarMaterialAlDomo).place(x=1, y=127, width = 800, height = 25)
        
        self.getMateriales() 

    def agregarMaterialAlDomo(self):
        id_material = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][0]
        nombre_material = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][1]
        tipo_material = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][2]
        precio_material = self.tabla_materiales.item(self.tabla_materiales.selection())['values'][3]

        c.execute('INSERT INTO material VALUES(?, ?, ?, ?)', (id_material, nombre_material, tipo_material, precio_material))
        conn.commit()
        self.get_materiales()

if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()
