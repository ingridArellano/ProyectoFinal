import random
import os

palabras=["MUSEO DE LOUVRE","PIERO DELLA FRANCESCA","BARROCO","IMPRESIONISMO","RAFAEL","ARTE ANTIGUO",
        "GÓTICO","MARIANO BENLLIURE","FLORENCIA","BARROCO","TOLEDO","ALEMANIA","CANTABRIA","ANTONIO SAURA","ANFITEATRO",
         "MUSEO DEL PRADO","MIRÓN","EN UN JARRÓN","BARROCO","MUSEO DEL LOUVRE","PABLO PICASSO","GÓTICO","RENACIMIENTO",
          "EL MIGUELETE ","JAPÓN","RUBENS ","TIZZIANO","ALBERTO CHURRIGUERA","MADRID","NUEVA YORK","ROMANTICISMO","MIGUEL ÁNGEL",
          "ROMANTICISMO","MUSEO DEL PRADO","VENECIA","MODERNISTA","ATENAS","BILBAO","SURREALISMO","RENACIMIENTO",
          "ROMÁNICO BARROCO GÓTICO","MIGUEL ÁNGEL","MUSEO DEL PRADO","LONDRES","GÓTICO","BARROCO","DAKOTA DEL SUR","ANTONIO GAUDÍ",
          "RENACIMIENTO","AUGUSTE RODIN"]

palabra=random.choice(palabras)


fallo0='''
            !====B
                 B
                 B
                 B
                 B
           ============
'''
fallo1='''
            !====B
            O    B
                 B
                 B
                 B
           ============
'''
fallo2='''
            !====B
          __O    B
                 B
                 B
                 B
           ============
'''
fallo3='''
            !====B
          __O__  B
                 B
                 B
                 B
           ============
'''
fallo4='''
            !====B
          __O__  B
            |    B
                 B
                 B
           ============
'''
fallo5='''
            !====B
          __O__  B
            |    B
           /     B
                 B
           ============
'''
fallo6='''
            !====B
          __O__  B
            |    B
           / \   B
                 B
           ============
'''

letras_correctas=" "
letras_Todas=" "
fallos=0

while True:

    os.system("cls")
    
    print("***********************************")
    print("************TEMA: ARTE*************")
    print("***********************************")
    if fallos==0:
        print(fallo0)
    elif fallos==1:
        print(fallo1)  
    elif fallos==2:
        print(fallo2)       
    elif fallos==3:
        print(fallo3) 
    elif fallos==4:
        print(fallo4)  
    elif fallos==5:
        print(fallo5) 
    elif fallos==6:
        print(fallo6)     
    print()    
   
   #mostramos el resultado que se va obteniendo
    resultado=""
    for letra in palabra:
        if letra in letras_correctas:
            resultado+=letra
            print(letra,end=" ")          
        else:
            resultado+=""
            print("*",end=" ")
    print()
    print() 
    #comprobamos si respondio correctamente o termino sus vidas
    if resultado==palabra:
        print("¡Haz ganado felicitaciones!")      
        break
    if fallos >5:
        print("Haz perdido")
        print("La respuesta  era: ",palabra)
        break
    #bucle para que el usuario ingrese la letra 
    while True:        
        letra_usuario=input("Ingrese una letra: ").upper()
        if len(letra_usuario)<1 or len(letra_usuario)>1:
            print("Introduce una sola letra")
        elif letra_usuario in letras_correctas:
            print("Esa letra ya la escribiste")
        elif not letra_usuario.isalpha():
            print("Introduce una letra no numeros ni signos(simbolos)")
        else:
            letras_Todas+=letra_usuario
            break  
    #comprobamos si la letra esta en palabra         
    if letra_usuario not in palabra:
        fallos+=1
    else:
        letras_correctas+=letra_usuario
  