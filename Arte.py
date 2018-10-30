print("Tema: Arte")
print (u"¿En qué museo se encuentra La Venus de Milo?")
Palabra='Museo del Louvre'
tuPalabra=''
vidas=10
while vidas>0:
    fallas=0
    for letra in Palabra:
        if letra in tuPalabra:
            print(letra, end =" "   )
        else :
            print("_",end =" ")    
            fallas+=1
    if fallas==0:
        print(u"¡Felicidades ganaste!")    
        break
    tuLetra=input("Introduce una letra: ")    
    tuPalabra+=tuLetra
    if tuLetra not in Palabra:
        vidas-=1
        print("Equivocacion")
        print("Tu tienes" +vidas+ "vidas")
    if vidas==0:
        print (u"¡Perdiste!")
else:
    print("Gracias por participar")        

    