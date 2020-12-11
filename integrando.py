from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    # connection dir property
    db_name = 'database.db'
    
    def __init__(self, window):
        self.wind = window
        #self.wind.config(bg = "white")
        self.wind.title('Agregar usuario')
        
        # Creando contenedor
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo usuario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Entrada de nombre 
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        # Entrada de nombre 
        Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
        self.apellido = Entry(frame)
        self.apellido.grid(row = 2, column = 1)

        # Correo Input
        Label(frame, text = 'Correo: ').grid(row = 3, column = 0)
        self.correo = Entry(frame)
        self.correo.grid(row = 3, column = 1)

        # Telefono Input
        Label(frame, text = 'Telefono: ').grid(row = 4, column = 0)
        self.telefono = Entry(frame)
        self.telefono.grid(row = 4, column = 1)

        # Button Add Product 
        ttk.Button(frame, text = 'Registrar usuario', command = self.agregarUsuario).grid(row = 5, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        # self.tree = ttk.Treeview(height = 10, columns = 2)
        # self.tree.grid(row = 4, column = 0, columnspan = 2)
        # self.tree.heading('#0', text = 'ID', anchor = CENTER)
        # self.tree.heading('#1', text = 'Nombre Apellido', anchor = CENTER)
        self.tree = ttk.Treeview(height=10,columns=("#1", "#2,", "#3,", "#4,"))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'ID', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Apellido', anchor = CENTER)
        self.tree.heading('#3', text = 'Correo', anchor = CENTER)
        self.tree.heading('#4', text = 'Telefono', anchor = CENTER)
        
        # Buttons
        ttk.Button(text = 'Borrar', command = self.borrarUsuario).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar', command = self.editarUsuario).grid(row = 5, column = 1, sticky = W + E)

        self.get_usuarios()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_usuarios(self):
        #Limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM usuario ORDER BY id_usuario DESC' 
        db_rows = self.run_query(query)
        
        #rellenando datos
        for row in db_rows:
            self.tree.insert('',0, text = row[0],values = (row[1], row[2], row[3], row[4]))
            #print(row)

    def validation(self):
        return len(self.nombre.get()) != 0 and len(self.apellido.get()) != 0 and len(self.correo.get()) != 0 and len(self.telefono.get()) != 0

    def agregarUsuario(self):
        if self.validation():
            query = 'INSERT INTO usuario VALUES(NULL, ?, ?, ?, ?)'
            parametros = (self.nombre.get(), self.apellido.get(), self.correo.get(), self.telefono.get())
            self.run_query(query, parametros)
            self.message['text'] = 'Datos ingresados correctamente..'
            self.nombre.delete(0, END)
            self.apellido.delete(0, END)
            self.correo.delete(0, END)
            self.telefono.delete(0, END)
        else:
            self.message['text'] = 'Faltan valores a ingresar..'
        self.get_usuarios()

    def borrarUsuario(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione un archivo'
            return
        self.message['text'] = ''
        id_usuario = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM usuario WHERE id_usuario = ?'
        self.run_query(query,(id_usuario, ))
        self.message['text'] = 'Usuario eliminado ..'
        self.get_usuarios()
    
    def editarUsuario(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione un archivo'
            return
        old_nombre = self.tree.item(self.tree.selection())['values'][0]
        old_apellido = self.tree.item(self.tree.selection())['values'][1]
        old_correo = self.tree.item(self.tree.selection())['values'][2]
        old_telefono = self.tree.item(self.tree.selection())['values'][3]
        self.edit_wind = Toplevel()
        self.edit_wind.title = "Editar usuario"

        #Old nombre
        Label(self.edit_wind, text = "Nombre anterior").grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_nombre), state = 'readonly').grid(row = 0, column = 2)
        #New nombre
        Label(self.edit_wind, text = "Nombre nuevo").grid(row = 1, column = 1)
        new_nombre = Entry(self.edit_wind)
        new_nombre.grid(row = 1, column = 2)

        #Old apellido
        Label(self.edit_wind, text = "Apellido anterior").grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_apellido), state = 'readonly').grid(row = 2, column = 2)
        #New apellido
        Label(self.edit_wind, text = "Apellido nuevo").grid(row = 3, column = 1)
        new_apellido = Entry(self.edit_wind)
        new_apellido.grid(row = 3, column = 2)

        #Old correo
        Label(self.edit_wind, text = "Correo anterior").grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_correo), state = 'readonly').grid(row = 4, column = 2)
        #New correo
        Label(self.edit_wind, text = "Correo nuevo").grid(row = 5, column = 1)
        new_correo = Entry(self.edit_wind)
        new_correo.grid(row = 5, column = 2)

        #Old telefono
        Label(self.edit_wind, text = "Telefono anterior").grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_telefono), state = 'readonly').grid(row = 6, column = 2)
        #New telefono
        Label(self.edit_wind, text = "Telefono nuevo").grid(row = 7, column = 1)
        new_telefono= Entry(self.edit_wind)
        new_telefono.grid(row = 7, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.editar_usuario(new_nombre.get(), old_nombre, new_apellido.get(),
         old_apellido, new_correo.get(), old_correo, new_telefono.get(), old_telefono)).grid(row=8, column=2, sticky = W + E)

    def editar_usuario(self, new_nombre, old_nombre, new_apellido, old_apellido, new_correo, old_correo, new_telefono, old_telefono):
        query = 'UPDATE usuario SET nombre = ?, apellido = ?, correo = ?, telefono = ? WHERE nombre = ? AND apellido = ? AND correo = ? AND telefono = ?'
        parametros = (new_nombre, new_apellido, new_correo, new_telefono, old_nombre, old_apellido, old_correo, old_telefono)
        self.run_query(query, parametros)
        self.edit_wind.destroy()
        self.message['text'] = 'Usuario editado correctamente'
        self.get_usuarios()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()