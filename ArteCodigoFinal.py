#TEMA: ARTE
import os
palabras=["MUSEO DE LOUVRE","PIERO DELLA FRANCESCA","BARROCO","IMPRESIONISMO","RAFAEL","ARTE ANTIGUO",
        "GÓTICO","MARIANO BENLLIURE","FLORENCIA","BARROCO","TOLEDO","ALEMANIA","CANTABRIA","ANTONIO SAURA","ANFITEATRO",
         "MUSEO DEL PRADO","MIRÓN","EN UN JARRÓN","BARROCO","MUSEO DEL LOUVRE","PABLO PICASSO","GÓTICO","RENACIMIENTO",
          "EL MIGUELETE ","JAPÓN","RUBENS ","TIZZIANO","ALBERTO CHURRIGUERA","MADRID","NUEVA YORK","ROMANTICISMO","MIGUEL ÁNGEL",
          "ROMANTICISMO","MUSEO DEL PRADO","VENECIA","MODERNISTA","ATENAS","BILBAO","SURREALISMO","RENACIMIENTO",
          "ROMÁNICO BARROCO GÓTICO","MIGUEL ÁNGEL","MUSEO DEL PRADO","LONDRES","GÓTICO","BARROCO","DAKOTA DEL SUR","ANTONIO GAUDÍ",
          "RENACIMIENTO","AUGUSTE RODIN"]
r=0
p=0|
preguntas=['1. ¿En qué museo se encuentra "La Venus de Milo"?  ','2. ¿Qué artista pintó "El sueño de Constantino"? ',
'3. ¿En qué movimiento cultural se encuentra Gian Lorenzo Bernini?','4. ¿En qué movimiento cultural se encuentra Van Gogh?',
'5. ¿Qué artista pintó "Triunfo de Galatea"?','6. Las pirámides de Guiza forman parte del:','7. ¿De qué estilo arquitectónico es la catedral de Sevilla?',
'8. ¿Quién esculpió la estatua ecuestre de Alfonso XII (1922) situada en el parque del Retiro en Madrid?',
'9. ¿En qué ciudad se encuentra "El David" de Miguel Ángel?','10. ¿En qué movimiento cultural se encuentra Vermeer?',
'11. ¿En qué ciudad se encuentra el lienzo "El entierro del conde de Orgaz"?','12. ¿Dónde se encuentra el Castillo Lichtenstein?',
'13. ¿Dónde se encuentra el Capricho de Gaudí?','14. ¿Qué pintor ilustró con imágenes el Quijote?','15. ¿Qué tipo de construcción era el Coliseo de Roma?',
'16. ¿En qué museo se encuentra "Judit en el banquete de Holofernes" de Rembrandt?','17. ¿Quién fue el escultor del "Discóbolo"?',
'18. ¿Dónde se encuentran los girasoles en "Los Girasoles" de Van Gogh?','19. ¿En qué movimiento cultural se encuentra Rubens?',
'20. ¿En qué museo se encuentra "La Vida de María de Médicis" de Rubens?','21. ¿Qué artista recibió el encargo del gobierno español para pintar el bombardeo de Guernica?',
'22. ¿De qué estilo arquitectónico es la catedral de Barcelona?','23. ¿En qué movimiento cultural se encuentra Tizziano?',
'24. ¿Cómo se llama la torre más famosa de la catedral de Valencia?','25. ¿Dónde se encuentra el "Gran Buda de Ushiku"?',
'26. ¿Quién pintó "Las Tres Gracias"?','27. ¿Quién pintó "Las 3 Edades del Hombre"?','28. ¿Qué artista diseñó la Plaza Mayor de Salamanca?',
'29. ¿Dónde se encuentra el Museo del Prado?','30. ¿Dónde se encuentra la Estatua de la Libertad?','31. ¿En qué movimiento cultural se encuentra Eugéne Delacroix?',
'32. ¿Qué artista pintó "El Diluvio Universal"?','33. ¿En qué movimiento cultural se encuentra Charles Garnier?',
'34. ¿En qué museo se encuentra "Carlos V en la batalla de Mühlberg" de Tiziano?','35. ¿En qué lugar se encuentra la Basílica de San Marcos?',
'36. ¿De qué estilo arquitectónico es la Sagrada Familia de Barcelona?','37. ¿En dónde se encuentra la Acrópolis?'
'38. ¿En qué ciudad se encuentra el Museo de Guggenheim?','39. ¿En qué movimiento cultural se encuentra Joan Miró?',
'40. ¿En qué movimiento cultural se encuentra Botticelli?','41. ¿De qué estilo arquitectónico es la catedral de Santiago de Compostela?',
'42. ¿Quién esculpió "La Piedad"?','43. ¿En qué museo se encuentra "El caballero de la mano en el pecho" de El Greco?',
'44. ¿En qué lugar se encuentra el Palacio de Windsor?','45. ¿De qué estilo arquitectónico es la Catedral de Milán?',
'46. ¿De qué estilo arquitectónico es la Fontana de Trevi?','47. El Monte Rushmore representa los primeros años de Historia de los Estados Unidos con las cabezas de cuatro presidentes de los Estados Unidos ¿dónde se encuentra?',
'48. ¿Quién diseñó el "Parque Güell" declarado patrimonio de la Humanidad? ','49. ¿De qué estilo arquitectónico es la Fachada de la Universidad de Salamanca?',
'50. "El Pensador" es una escultura de:']
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
    palabra=palabras[r]
    pregunta=preguntas[p]
    print("***********************************")
    print("*********** TEMA: ARTE ************")
    print("***********************************")
    print(pregunta)
     
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
     #Mostramos el resultado que se va obteniendo
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
        print() 
        r+=1 
        p+=1 
        letras_Todas=' '
        letras_correctas=' '
        fallos=0
        
    if fallos >5:
        print("Haz perdido")
        print("La respuesta  era: ",palabra)
        print()
        r+=1 
        p+=1 
        letras_Todas=' '
        letras_correctas=' '
        fallos=0
       
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
    #comprobamos si la letra esta en paldabra         
    if letra_usuario not in palabra:
        fallos+=1
    else:
        letras_correctas+=letra_usuario