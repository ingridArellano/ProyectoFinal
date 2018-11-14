#TEMA: CIENCIA
import os
palabras=["CINCO PARES","NUEZ","LA PROPIEDAD CONMUTATIVA","CUCARACHA","AGUILUCHO","ARCO","NOVENTA","TIMBRE","FUSIÓN","FÉMUR","CLOROFILA",
"MERIDIANO DE GREENWICH","CENTÍGRADOS","DOS","SATURNO","AVES","JABATO","FLEMMING","MOLÉCULAS","POSITIVA","OVINA","CONDENSACIÓN","TRECIENTOS MIL KILOMETROS POR SEGUNDO",
"MÍNIMO COMÚN MÚLTIPLO","PLOMO","ENERGÍA ATÓMICA","ENTRE SEIS Y SIETE METROS","BREVA","FOSAS NASALES","EL TIBURÓN BALLENA","SETECIENTOS VEINTE","VÉRTEBRAS",
"MOL","POR LOS CROMATÓFOROS","VELOCIDAD","LAS PLANTAS VERDES","MERCURIO","SEIS","LA ROTACIÓN DE LA TIERRA ALREDEDOR DEL SOL","QUINQUENIO",
"MIL KILOGRAMOS","MÁXIMO COMÚN DIVISOR","LA INSULINA","SARDINA"]
r=0
p=0
preguntas=['1. ¿Cuántas patas tienen los cangrejos?','2. ¿Cómo se llama el fruto del nogal?',
'3. El orden de los sumandos no altera el producto: esta afirmación corresponde con','4. ¿Qué animal podría sobrevivir a una explosión nuclear?',
'5. ¿Cómo se llaman las crías del águila?','6. ¿Cómo se llama la parte de la circunferencia comprendida entre dos puntos?',
'7. ¿Cuántos grados tiene un ángulo recto?','8. ¿Qué propiedad del sonido permite distinguir entre dos notas musicales tocadas por dos instrumentos diferentes?',
'9. La temperatura a la cual la materia pasa de estado sólido a estado líquido se denomina','10. ¿Cuál es el hueso más largo del ser humano?',
'11. La ciencia o rama de la biología que estudia los vegetales se denomina',
'12. ¿Cómo se llama el pigmento verde que le da el color característico a las plantas?','13. La longitud de un punto geográfico es la distancia entre éste y',
'14. La escala de temperatura utilizada en España se llama','15. ¿Cuál es el único número que es par y primo a la vez?',
'16. ¿Qué planeta es famoso por los anillos que lo rodean?','17. ¿Qué tipos de animales tienen molleja?','18. La cría del jabalí recibe el nombre de:',
'19. ¿Quién descubrió la penicilina?','20. La combinación de dos átomos del mismo elemento da como resultado','21. ¿Cómo es la carga del protón?',
'22. ¿Qué tipo de ganadería se ocupa de las ovejas?','23. El paso del estado de la materia que se encuentra en forma gaseosa a forma líquida se denomina',
'24. ¿Cuál es la velocidad máxima de la luz en el vacío?','25. ¿Cómo se llama al menor número natural que es múltiplo de dos o más números?',
'26. ¿Cuál es el elemento químico cuyo símbolo es Pb?','27. ¿Cuál de las siguientes fuentes no es una energía renovable?',
'28. El intestino delgado tiene una longitud aproximada de','29. ¿Cuál es el primer fruto de la higuera?','30. Los agujeros de la nariz se llaman',
'31. ¿Cuál de los siguientes tiburones tiene mayor tamaño?','32. ¿Cuántas vueltas da el segundero en una vuelta completa en un reloj de doce horas?',
'33. Los huesos de la columna vertebral se llaman','34. ¿Cómo se llama el peso molecular de una sustancia?','35. ¿Por qué los camaleones cambian de color?',
'36. ¿Cuál es la magnitud que relaciona espacio y tiempo?','37. ¿Quiénes realizan la nutrición autótrofa?',
'38. ¿Qué sustancia se encuentra en el interior de un termómetro?','39. ¿Cuántas patas tiene una abeja?','40. El movimiento de traslación consiste en',
'41. ¿Cómo se denomina a un periodo de 5 años?','42. ¿Cuántos kilos hay en una tonelada?',
'43. ¿Cómo se llama al mayor número que divide dos o más números sin dejar resto?','44. ¿Qué líquido segrega el páncreas?',
'¿Cuál es un pez propio de alta mar?']

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
    print("*********** TEMA: CIENCIA *********")
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