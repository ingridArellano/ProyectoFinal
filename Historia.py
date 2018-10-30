historia=["Punicas", "Cortes Generales", "perro"]
import random
num=random.randit(0,2)
bandera=True
while (bandera):
    opcion=raw_input("Elija una opción:\n1-Numero de letras\n2-Contar letra\n3-Posicion primera aparició\n4-Posicion ultima aparición\n5-Adivinar historia\n6-Salir\n")
    op=int(opcion)
    if(op==1):
        tam=len(historia(num))
        print "Numeros de letras son:", tam
    if (op==2):
        letra=raw_inpt("Ingrese una letra: ")
        letra=letra.strip()
        numLetras=historia[num].count(letra)
        if letra<0:
            print "La letra ",letra," no se encuentra"
        else:
            print "El numero de ",letra, "son: ", numLetras
    if (op==3):
        letra=raw_input("Ingrese una letra: ")
        letra=letra.strip()
        pos=historia[num].find(letra)
        if pos<0:
            print "La letra ",letra, "no esta en la palabra"
        else:
            print "La letra ",letra, "se encuentra en la posicion ",pos+1
    if(op==4:)
        letra=raw_input("Ingrese una letra: ")
        letra=letra.strip()
        pos=frutas[num].rfind(letra)
        if pos<0:
            print "La letra ",letra, "no esta en la palabra"
        else:
            print "La letra ", letra, "esta en la posicion",pos+1
    if(op==5:)
        palabra=raw_input("Responda la pregunta: ")
        palabra=palabra.strip()
        if(palabra==historia[num]):
            print "Felicidades ganaste\nLa fruta era", historia[num]
            bandera=False
        else:
            print "Vuelve a intentarlo"
    if (op==6):
        bandera=False
