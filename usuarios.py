from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Manejo de usuarios')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo usuario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Nombre Input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        # Apellido Input
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
        ttk.Button(frame, text = 'Registrar usuario', command = self.add_product).grid(row = 5, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Apellido', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Filling the Rows
        self.get_products()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM usuario ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # User Input Validation
    def validation(self):
        return len(self.nombre.get()) != 0 and len(self.apellido.get()) != 0 and len(self.correo.get()) != 0 and len(self.telefono.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO usuario VALUES(NULL, ?, ?, ?, ?)'
            parameters =  (self.nombre.get(), self.apellido.get(), self.correo.get(), self.telefono.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Usuario {} added Successfully'.format(self.nombre.get())
            self.nombre.delete(0, END)
            self.apellido.delete(0, END)
            self.correo.delete(0, END)
            self.telefono.delete(0, END)
        else:
            self.message['text'] = 'Name and Price is Required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM usuario WHERE nombre = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Usuario {} eliminado.'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Debe seleccionar un usuario.'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar usuario'

        # Old Name
        Label(self.edit_wind, text = 'Antiguo nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old apellido
        Label(self.edit_wind, text = 'Antiguo apellido:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # New apellido
        Label(self.edit_wind, text = 'Nuevo apellido:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        # Old Correo
        Label(self.edit_wind, text = 'Antiguo correo:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 4, column = 2)
        # New Correo
        Label(self.edit_wind, text = 'Nuevo correo:').grid(row = 5, column = 1)
        new_correo= Entry(self.edit_wind)
        new_correo.grid(row = 5, column = 2)

        # Old telefono
        Label(self.edit_wind, text = 'Antiguo telefono:').grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 6, column = 2)
        # New telefono
        Label(self.edit_wind, text = 'Nuevo telefono:').grid(row = 7, column = 1)
        new_correo= Entry(self.edit_wind)
        new_correo.grid(row = 7, column = 2)

        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 8, column = 2, sticky = W+E)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
