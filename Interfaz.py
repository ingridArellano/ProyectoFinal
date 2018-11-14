from tkinter import *

raiz= Tk()
raiz.title("AHORCADO")
raiz.resizable(False,False)
raiz.geometry('350x350')

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Labels:
miLabel = Label(miFrame, text=" BIENVENIDOS AL JUEGO ")
miLabel.pack()1

miLabel2 = Label(miFrame, text=" Escoja un tema sobre Cultura General: ")
miLabel2.pack()

# Botones:
arteBoton = Button(raiz, text="Arte")
arteBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
arteBoton.config(bg="light blue")
arteBoton.config(cursor="hand2")

cienciaBoton = Button(raiz, text="Ciencia")
cienciaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
cienciaBoton.config(bg="pink")
cienciaBoton.config(cursor="hand2")

historiaBoton = Button(raiz, text="Historia")
historiaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
historiaBoton.config(bg="purple")
historiaBoton.config(cursor="hand2")

lenguajeBoton = Button(raiz, text="Lenguaje")
lenguajeBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
lenguajeBoton.config(bg="fuchsia")
lenguajeBoton.config(cursor="hand2")

geografiaBoton = Button(raiz, text="Geografía")
geografiaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
geografiaBoton.config(bg="Grey")
geografiaBoton.config(cursor="hand2")

respuestaBoton = Button(raiz, text="Enviar respuesta") #Para agregarle una acción ponemos command=Accioncreada
respuestaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)


raiz.mainloop()



#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class Aplicacion():
    ventana = 0
    posx_y = 0
        
    def __init__(self):                             
        self.raiz = Tk()
        self.raiz.geometry('300x200+500+50')
        self.raiz.resizable(0,0)
        self.raiz.title("AHORCADO")
        boton = ttk.Button(self.raiz, text='Abrir', 
                           command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()

    def abrir(self):
        ''' Construye una ventana de diálogo '''
        
        self.dialogo = Toplevel()
        Aplicacion.ventana+=1
        Aplicacion.posx_y += 50
        tamypos = '200x100+'+str(Aplicacion.posx_y)+ \
                  '+'+ str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0,0)
        ident = self.dialogo.winfo_id()
        titulo = str(Aplicacion.ventana)+": "+str(ident)
        self.dialogo.title(titulo)
        boton = ttk.Button(self.dialogo, text='Cerrar', 
                           command=self.dialogo.destroy)   
        boton.pack(side=BOTTOM, padx=20, pady=20)
        
        # Convierte la ventana 'self.dialogo' en 
        # transitoria con respecto a su ventana maestra 
        # 'self.raiz'.
        # Una ventana transitoria siempre se dibuja sobre
        # su maestra y se ocultará cuando la maestra sea
        # minimizada. Si el argumento 'master' es
        # omitido el valor, por defecto, será la ventana
        # madre.
        
        self.dialogo.transient(master=self.raiz)

        # El método grab_set() asegura que no haya eventos 
        # de ratón o teclado que se envíen a otra ventana 
        # diferente a 'self.dialogo'. Se utiliza para 
        # crear una ventana de tipo modal que será 
        # necesario cerrar para poder trabajar con otra
        # diferente. Con ello, también se impide que la 
        # misma ventana se abra varias veces. 
        
        self.dialogo.grab_set()
        self.raiz.wait_window(self.dialogo)
    
def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()