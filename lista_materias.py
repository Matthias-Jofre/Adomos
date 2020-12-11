from tkinter import ttk
from tkinter import *

import sqlite3

class Materiales:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        #self.wind.config(bg = "white")
        self.wind.title('Lista de materiales')

        # Creando contenedor
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo material')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Entrada de nombre 
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        # Entrada de tipo
        Label(frame, text = 'Tipo: ').grid(row = 2, column = 0)
        self.tipo = Entry(frame)
        self.tipo.grid(row = 2, column = 1)

        # cantidad Input
        Label(frame, text = 'Cantidad: ').grid(row = 3, column = 0)
        self.cantidad = Entry(frame)
        self.cantidad.grid(row = 3, column = 1)

        # precio Input
        Label(frame, text = 'Precio: ').grid(row = 4, column = 0)
        self.precio = Entry(frame)
        self.precio.grid(row = 4, column = 1)

        # Button Add Product 
        ttk.Button(frame, text = 'Registrar material', command = self.agregarMaterial).grid(row = 5, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)


        
        # Buttons
        ttk.Button(text = 'Borrar', command = self.borrarMaterial).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar', command = self.editarMaterial).grid(row = 5, column = 1, sticky = W + E)

        self.get_materiales()        

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_materiales(self):
        #Limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM materiales ORDER BY id_material DESC' 
        db_rows = self.run_query(query)
        
        #rellenando datos
        for row in db_rows:
            self.tree.insert('',0, text = row[0],values = (row[1], row[2], row[3], row[4]))
            #print(row)    

    def validation(self):

        return len(self.nombre.get()) != 0 and len(self.tipo.get()) != 0 and len(self.cantidad.get()) != 0 and len(self.precio.get()) != 0

    def agregarMaterial(self):
        if self.validation():
            query = 'INSERT INTO materiales VALUES(NULL, ?, ?, ?, ?)'
            parametros = (self.nombre.get(), self.tipo.get(), self.cantidad.get(), self.precio.get())
            self.run_query(query, parametros)
            self.message['text'] = 'Datos ingresados correctamente..'
            self.nombre.delete(0, END)
            self.tipo.delete(0, END)
            self.cantidad.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.message['text'] = 'Faltan valores a ingresar..'
        self.get_materiales()

    def borrarMaterial(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione un archivo'
            return
        self.message['text'] = ''
        id_material = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM materiales WHERE id_material = ?'
        self.run_query(query,(id_material, ))
        self.message['text'] = 'Material eliminado ..'
        self.get_materiales()

    def editarMaterial(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione un material'
            return
        old_nombre = self.tree.item(self.tree.selection())['values'][0]
        old_tipo = self.tree.item(self.tree.selection())['values'][1]
        old_cantidad = self.tree.item(self.tree.selection())['values'][2]
        old_precio = self.tree.item(self.tree.selection())['values'][3]
        self.edit_wind = Toplevel()
        self.edit_wind.title = "Editar material"

        #Old nombre
        Label(self.edit_wind, text = "Nombre anterior").grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_nombre), state = 'readonly').grid(row = 0, column = 2)
        #New nombre
        Label(self.edit_wind, text = "Nombre nuevo").grid(row = 1, column = 1)
        new_nombre = Entry(self.edit_wind)
        new_nombre.grid(row = 1, column = 2)

        #Old tipo
        Label(self.edit_wind, text = "Tipo anterior").grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_tipo), state = 'readonly').grid(row = 2, column = 2)
        #New tipo
        Label(self.edit_wind, text = "Tipo nuevo").grid(row = 3, column = 1)
        new_tipo = Entry(self.edit_wind)
        new_tipo.grid(row = 3, column = 2)

        #Old cantidad
        Label(self.edit_wind, text = "Cantidad anterior").grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_cantidad), state = 'readonly').grid(row = 4, column = 2)
        #New cantidad
        Label(self.edit_wind, text = "Cantidad nueva").grid(row = 5, column = 1)
        new_cantidad = Entry(self.edit_wind)
        new_cantidad.grid(row = 5, column = 2)

        #Old precio
        Label(self.edit_wind, text = "Precio anterior").grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_precio), state = 'readonly').grid(row = 6, column = 2)
        #New precio
        Label(self.edit_wind, text = "Precio nuevo").grid(row = 7, column = 1)
        new_precio= Entry(self.edit_wind)
        new_precio.grid(row = 7, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.editar_material(new_nombre.get(), old_nombre, new_tipo.get(),
         old_tipo, new_cantidad.get(), old_cantidad, new_precio.get(), old_precio)).grid(row=8, column=2, sticky = W + E)

    def editar_material(self, new_nombre, old_nombre, new_tipo, old_tipo, new_cantidad, old_cantidad, new_precio, old_precio):
        query = 'UPDATE materiales SET nombre = ?, tipo = ?, cantidad = ?, precio = ? WHERE nombre = ? AND tipo = ? AND cantidad = ? AND precio = ?'
        parametros = (new_nombre, new_tipo, new_cantidad, new_precio, old_nombre, old_tipo, old_cantidad, old_precio)
        self.run_query(query, parametros)
        self.edit_wind.destroy()
        self.message['text'] = 'Material editado correctamente'
        self.get_materiales()

if __name__ == '__main__':
    window = Tk()
    application = Materiales(window)
    window.mainloop() 