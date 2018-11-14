#GEOGRAFÍA
import os
palabras=["ALICANTINO","COPENHAGUE","TOLEDO","JAÉN","CIUDAD REAL","SEVILLA","OSLO","FRANCIA","DANUBIO","SEVILLANO","SANTANDER","PERÚ COLOMBIA Y BRASIL",
"TINERFEÑO","ANDALUCÍA","ITALIA","PYONGYANG","VALENCIA","JIENESE","LÍBANO","ALICANTE","VARSOVIA","TAIWAN","RIGA","SEÚL","SERBIA","PORTUGAL","ITALIA","ZAMORA",
"CEUTÍ","SEGOVIANO","TRAJO","VIGO","DUBLÍN","ARIZONA","VALLADOLID","REPÚBLICA CHECA","ABULENSE","TUROLENSE","GUADALQUIVIR","GUIPUZCOANO","BURGALÉS","ZAMORANO",
"OSCENSE","BADAJOZ","NÁPOLES","CÁDIZ","ASIA","CASTILLA LA MANCHA","MAR MEDITERRÁNEO","BERLÍN"]
r=0


p=0
preguntas=["1. El gentilicio de la provincia de Alicante es","2. La capital de la comunidad autónoma de Castilla la Mancha es",
"3. Úbeda pertenece a la provincia de","4. Puertollano pertenece a la provincia de",
"5. Écija pertenece a la provincia de","6. La capital de Noruega es","7. ¿Dónde se encuentra el Cabo de San Mateo?",
"8. ¿Cuál es el río europeo que atraviesa un mayor número de países?","9. El gentilicio de la provincia de Sevilla es",
"10. Laredo pertenece a la provincia de","11. Los países por los que pasa el Amazonas son","El gentilicio de Tenerife es",
"12. La ciudad de Sevilla forma parte de la comunidad autónoma de","13. ¿Cuál de los siguientes países no tiene frontera con España?",
"14. La capital de Corea del Norte es","¿Qué ciudad es conocida como la ciudad del Turia?",
"15. El gentilicio de la provincia de Jaén es","Beirut es la capital de","16. Benidorm pertenece a la provincia de","17. La capital de Polonia es",
"18. Taipei es la capital de","19. La capital de Letonia es","20. La capital de Corea del Sur es","21. Belgrado es capital de",
"22. La provincia de Salamanca limita al oeste con","23. ¿Dónde se encuentran los montes Apeninos?","24. El Lago de Sanabria pertenece a la provincia de",
"25. El gentilicio de la provincia de Ceuta es","26. El gentilicio de la provincia de Segovia es","27. ¿De qué río es afluente el Manzanares?",
"28. Indica cuál de las siguientes no es capital de provincia","29. La capital de Irlanda es","30. ¿Dónde se encuentra el Cañón del Colorado?",
"31. La capital de la comunidad autónoma de Castilla y León es","32. Praga es la capital de","33. El gentilicio de la provincia de Ávila es",
"34. El gentilicio de la provincia de Teruel es","35. Por la ciudad de Sevilla pasa el río","36. El gentilicio de la provincia de Guipúzcoa es",
"37. El gentilicio de la provincia de Burgos es","38. El gentilicio de la provincia de Zamora","39. El gentilicio de la provincia de Huesca es",
"40. El Guadiana pasa por","El Monte Vesubio se encuentra en","50. ¿A qué provincia pertenece Algeciras?",
"51. ¿Cuál es el continente más extenso del planeta Tierra?","52. La ciudad de Toledo forma parte de la comunidad autónoma de",
"53. La Isla de Mallorca se encuentra bañada por","La capital de Alemania es"]

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
    #os.system("cls")
    palabra=palabras[r]
    pregunta=preguntas[p]

    print("***********************************")
    print("************TEMA : GEOFRAFÍA*************")
    print("***********************************")
    print()
    if r==p:
        print(pregunta)
        p+=1

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
    #comprobamos si respondio correctamente o termino sus vidas
    if resultado==palabra:    
        print("¡Haz ganado felicitaciones!")  
        print()
       # break
    if fallos >5:
        print("¡Haz perdido!")
        print("La respuesta  era: ",palabra)
        print()
        #break 

    if resultado==palabra or fallos >5:
        r+=1