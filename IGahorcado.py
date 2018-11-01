from tkinter import *

raiz= Tk()
raiz.title("AHORCADO")
raiz.resizable(False,False)
raiz.geometry("350x350")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Labels:
miLabel = Label(miFrame, text=" BIENVENIDOS AL JUEGO ")
miLabel.pack()

miLabel2 = Label(miFrame, text=" Escoja un tema de Cultura General: ")
miLabel2.pack()

# Botones:
arteBoton = Button(raiz, text="Tema: Arte")
arteBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
arteBoton.config(bg="light blue")
arteBoton.config(cursor="hand2")

cienciaBoton = Button(raiz, text="Tema: Ciencia")
cienciaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
cienciaBoton.config(bg="pink")
cienciaBoton.config(cursor="hand2")

historiaBoton = Button(raiz, text="Tema: Historia")
historiaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
historiaBoton.config(bg="purple")
historiaBoton.config(cursor="hand2")

lenguajeBoton = Button(raiz, text="Tema: Lenguaje")
lenguajeBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
lenguajeBoton.config(bg="fuchsia")
lenguajeBoton.config(cursor="hand2")

geografiaBoton = Button(raiz, text="Tema: Geografía")
geografiaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)
geografiaBoton.config(bg="Grey")
geografiaBoton.config(cursor="hand2")

respuestaBoton = Button(raiz, text="Enviar respuesta") #Para agregarle una acción ponemos command=Accioncreada
respuestaBoton.pack(side="top", fill="both", expand="False", padx=10, pady=10)


raiz.mainloop()