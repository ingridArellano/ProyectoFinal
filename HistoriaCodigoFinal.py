#TEMA: HISTORIA
import os
palabras=["PÚNICAS","CORTES GENERALES","REINO UNIDO CONTRA ESPAÑA Y FRANCIA","MIL NOVECIENTOS OCHENTA Y NUEVE","MIL NOVECIENTOS CATORCE","ARGENTINA",
"VALENCIA","TRATADO DE VERSALLES","TEXTIL","CARLOS II","LA GUERRA CIVIL","TRANSPORTE DE MERCANCÍAS","FEUDALISMO","EL DESEADO",
"CAÍDA DEL IMPERIO ROMANDO DE OCCIDENTE","DIOCLECIANO","CALÍGULA","LA GUERRA DE LA INDEPENDECIA","MIL CUATROCIENTOS NOVENTA Y DOS","ESPAÑA Y PORTUGAL",
"AL NORESTE","PAZ DE WESTFALIA","ALTAS TASAS DE MORTALIDAD Y NATALIDAD","DEMOGRÁFICA","TURCOS","REVOLUCIÓN FRANCESA","BURGOS",
"LA MUERTE SIN DESCENDENCIA DE CALOR II DE ESPAÑA","MIL NOVECIENTOS TREINTA Y NUEVE Y MIL NOVECIENTOS SETENTA Y CINCO",
"FERNANDO II DE ARAGÓN E ISABEL I DE CASTILLA","LA EDAD MEDIA","LA SEGUNDA GUERRA MUNDIAL","EL CID CAMPEADOR","INGLATERRA","EL DESCUBRIMIENTO DE AMÉRICA",
"2 DE MAYO DE MIL OCHOCIENTOS OCHO","ARISTOCRACIA","MIL NOVECIENTOS TREINTA Y UNO Y MIL NOVECIENTOS TREINTA Y NUEVE","REVOLUCIÓN INDUSTRIAL",
"DOS CIENTOS DIECIOCHO ANTES DE CRISTO","ENCONTRAR OTRA RUTA ALTERNATIVA A ORIENTE","AMÉRICA","PAPIRO","BURGUESES","LA CÁDIZ EN MIL OCHOCIENTOS DOCE",
"PATRICIOS"]
r=0
p=0
preguntas=['1. ¿Qué nombre recibieron las guerras entre Roma y Cartago?','2. ¿Por quién fue proclamada la Primera República Española el 11 de febrero de 1873?',
'3. ¿Quiénes se enfrentaron en la Batalla de Trafalgar?','4. ¿Con qué nombre fue denominada la Península Ibérica durante la dominación musulmana?',
'5. ¿Cuándo tuvo lugar la caída del Muro de Berlín?','6. ¿Cuándo comenzó la Primera Guerra Mundial?',
'7. ¿Cuál fue el primer país en independizarse de España?',
'8. ¿Dónde tuvo lugar la rebelión de las Germanías que desembocó en un levantamiento de armas contra el emperador Carlos I?',
'9. ¿Cómo se denominó el tratado de paz firmado al final de la Primera Guerra Mundial?',
'10. ¿Qué tipo de industria fue la que mejor simbolizó el desarrollo técnico y de desarrollo en Inglaterra durante el siglo XVIII?',
'11. ¿Qué último Rey de la casa de los Austria reinó en España?','12. La batalla del Ebro fue una batalla librada durante',
'13. ¿Cuál fue el primer uso que tuvo el ferrocarril a principios del siglo XIX? ',
'14. ¿Cuál fue el sistema político predominante en la Europa occidental de la Edad Media?','15. ¿Con qué nombre ha pasado Fernando VII a la Historia?',
'16. ¿Con qué acontecimiento comienza la Edad Media?','17. ¿Qué emperador dividió al imperio romano en oriente y occidente?',
'18. ¿Qué emperador Romano hizo senador a su caballo?','19. ¿Con qué acontecimiento dio comienzo en España a la Edad Contemporánea?',
'20. ¿En qué año tuvo lugar el descubrimiento de América?','21. ¿Qué países firmaron el Tratado de Tordesillas en 1494?',
'22. ¿En qué zona de la Península Ibérica se instalaron pueblos celtas?','24. ¿Qué acuerdo puso fin a la guerra de los Treinta Años en 1648?',
'25. ¿Qué caracterizó el régimen demográfico antiguo?','26. En la Revolución Industrial se produjo: una revolución agraria, tecnológica, de transporte y',
'27. La batalla de Lepanto fue ganada por los españoles contra los',
'28. ¿Cuál fue el cambio político más importante que se produjo en Europa a finales del siglo XVIII?','29. ¿En qué provincia nació el Cid Campeador?',
'30. ¿Cuál fue la causa fundamental del inicio de la Guerra de Sucesión Española?','31. La dictadura de Franco ocurrió entre',
'32. ¿Quiénes fueron los Reyes Católicos?','33. El Imperio bizantino pervivió durante toda','34. ¿Cuál ha sido la guerra más sangrienta de la historia?',
'35. ¿Cómo era conocido Rodrigo Díaz de Vivar?','36. ¿En qué país se sitúa el origen de la Revolución Industrial del siglo XVIII?',
'37. ¿Qué acontecimiento marca el inicio de la Edad Moderna?','38. El levantamiento del pueblo español contra Napoleón que invadía España tuvo lugar el',
'39. ¿Qué tipo de gobierno comienza en la Antigua Grecia que otorgaba el poder a la cúpula militar?','40. La Segunda República se extendió entre los años',
'41. ¿Cómo fue llamado el periodo histórico comprendido entre la segunda mitad del siglo XVIII y principios del XIX en el que se llevaron a cabo transformaciones socioeconómicas, tecnológicas y culturales de la historia de la humanidad?',
'42. ¿En qué año comenzó la conquista por parte de los romanos a España?','43. ¿Cuál era el principal propósito de Cristóbal Colón en su viaje hacia América?',
'44. El Imperio incaico fue un estado precolombino situado en','45. ¿Cómo se le llamó el soporte que utilizaron los antiguos egipcios para la escritura?',
'46. ¿Cuál de estos no es un grupo social de Roma?','47. ¿Cuál fue la primera Constitución española?',
'48. ¿Cómo se llamaban a los descendientes de los primeros pobladores de Roma?']

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
    print("*********** TEMA: HISTORIA*********")
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