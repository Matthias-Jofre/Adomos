from tkinter import ttk
from tkinter import *

import sqlite3

conn = sqlite3.connect('pruebas.db')
c = conn.cursor()

class Login:

    db_name = 'pruebas.db'


    def __init__(self, window):

        self.wind = window
        self.wind.title('Login')
        self.wind.geometry('400x200')
        self.wind.resizable(0, 0)

        self.et_nombre = Label(self.wind, text="Ingrese su rut:")
        self.et_nombre.place(x=10, y=10)

        self.ent_nombre = Entry(self.wind)
        self.ent_nombre.place(x=15, y=30)

        self.et_contraseña = Label(self.wind, text="Ingrese su contraseña:")
        self.et_contraseña.place(x=10, y=50)

        self.ent_contraseña = Entry(self.wind, show = "*")
        self.ent_contraseña.place(x=15, y=70)

        self.bot_login = Button(self.wind, text="Login",
                                command=self.InsertarDatos)
        self.bot_login.place(x=10, y=100)

        self.bot_exit = Button(self.wind, text="Salir", command = self.ValidarLogin)
        self.bot_exit.place(x=100, y=100)

        # self.radioLeido = IntVar()
        # self.radioLeido1 = Radiobutton(self.wind, text = 'Ejemplo 1', variable = self.radioLeido, value = 1, state = DISABLED)
        # self.radioLeido1.place(x = 300, y = 10)

        self.et_nombre1 = Entry(self.wind, state = DISABLED)
        self.et_nombre1.place(x = 200, y = 30)

        self.et_apellido1 = Entry(self.wind, state = DISABLED)
        self.et_apellido1.place(x = 200, y = 60)

        self.et_rut1 = Entry(self.wind, state = DISABLED)
        self.et_rut1.place(x = 200, y = 90)

        self.et_correo1 = Entry(self.wind, state = DISABLED)
        self.et_correo1.place(x = 200, y = 120)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def InsertarDatos(self):
        sql = "insert into nombres values(?,?)"
        val = (self.ent_nombre.get(), self.ent_contraseña.get())
        self.run_query(sql, val)
        print(val)

    def TraerDatos(self, query, nombre):
        with sqlite3.connect(self.db_name) as conn:
            #query = "select * from nombres where nombre = 'Matias'"
            cursor = conn.cursor()
            result = cursor.execute(query, nombre)
            conn.commit()
            # for row in result:
            #     print(row)
        return  result

    def ValidarLogin(self): 
        print(c.execute("select rut, nombre, apellido, correo from usuario where rut = ? and contraseña = ?",
                        (self.ent_nombre.get(), self.ent_contraseña.get())))
        data = c.fetchall()
        # ewe = tuple(data)
        # print(type(data))
        if data:
            for row in data:
                row[0]
            #self.radioLeido1.config(state = NORMAL)
            self.et_nombre1.config(textvariable = StringVar(self.wind, value=row[0]))
            self.et_apellido1.config(textvariable = StringVar(self.wind, value=row[1]))
            self.et_rut1.config(textvariable = StringVar(self.wind, value=row[2]))
            self.et_correo1.config(textvariable = StringVar(self.wind, value=row[3]))
            print('no esta vacia')
            print(row[(0)])
            self.ent_nombre.delete(0, END)
            self.ent_contraseña.delete(0, END)
            return True
        else:
            print('esta vacia')
            return False
    
         #print(data)
        # parametros = (self.ent_nombre.get())
        # print(parametros)
        # print(self.TraerDatos(sql, parametros))
        # # for ro in row:
        # #     print(ro)    

    def Exit(self):
        self.wind.destroy()

if __name__ == '__main__':
    window = Tk()
    application = Login(window)
    window.mainloop()
