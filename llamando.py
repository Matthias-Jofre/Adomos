from tkinter import ttk
from tkinter import *
from integrando import Product

class ventanaPrincipal:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Agregar usuario')

        frame = LabelFrame(self.wind, text = 'Abrir ventanas')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
            
        ttk.Button(frame, text = 'Registrar usuario', command = self.abrirVentana).grid(row = 5, columnspan = 2, sticky = W + E)

    def abrirVentana(self):
        # self.edit_wind = Tk()
        self.edit_win = Product(window)
        
        #self.edit_wind.title = "Editar usuario"


if __name__ == '__main__':
    window = Tk()
    application = ventanaPrincipal(window)
    window.mainloop()