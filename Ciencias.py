print("Tema: Ciencias")
print(u"Pregunta 1: ¿Cuántas patas tienen los cangrejos?")

respuestacorrecta = "Cinco pares"
respuestadelusuario = input ('')
vidas = 10

while vidas > 0:

    fallas = 0
    for letra in respuestacorrecta:
        if letra in respuestadelusuario:
            print (respuestadelusuario)
    
else:
    print("Falla")