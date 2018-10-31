import random
import os

palabras=["MUSEO DE LOUVRE","PIERO DELLA FRANCESCA","BARROCO"]

palabras=random.choice(palabras)

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
    
    print("************Tema: Arte******************")
    print ("¿En qué museo se encuentra La Venus de Milo?")
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

    

    for letra in palabras:
        if letra in letras_correctas:
            print(letra,end=" ")
               
        else:
            print("*",end=" ")
            

 
    print()
    print()
   


    if letras_correctas==palabras:
        print("¡Haz ganado felicitaciones!")      
        break

    if fallos >5:
        print("La respuesta  era: ",palabras)
        print("Haz perdido")
        break

    while True:
       
        letra_usuario=input("Introduce una letra: ") .upper()
        if len(letra_usuario)<1 or len(letra_usuario)>1:
            print("Introduce una sola letra")
        elif letra_usuario in letras_correctas:
            print("Esa letra ya la escribiste")
        elif not letra_usuario.isalpha():
            print("Introduce una letra no numeros ni signos(simbolos)")
        else:
            letras_Todas+=letra_usuario
            break
    if letra_usuario not in palabras:
        fallos+=1
    else:
        letras_correctas+=letra_usuario

  