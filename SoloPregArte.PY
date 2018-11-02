import os
columnas=50
renglones=1   
os.system("cls")
a=[([0]*columnas )for renglones in range(renglones)]  
for r in range(0,renglones):
    for c in range(0,columnas):
        if c==0:
            a[r][c]=input('1. ¿En qué museo se encuentra "La Venus de Milo"?  ')   
        print()     
        if c==1:
            a[r][c]=input('2. ¿Qué artista pintó "El sueño de Constantino"?  ')
        if c==2:
            a[r][c]=input('3. ¿En qué movimiento cultural se encuentra Gian Lorenzo Bernini?  ')
        if c==3:
            a[r][c]=input('4. ¿En qué movimiento cultural se encuentra Van Gogh?  ')
        if c==4:
            a[r][c]=input('5. ¿Qué artista pintó "Triunfo de Galatea"?  ')
        if c==5:
            a[r][c]=input('6. Las pirámides de Guiza forman parte del:  ')
        if c==6:
            a[r][c]=input('7. ¿De qué estilo arquitectónico es la catedral de Sevilla? ')
        if c==7:
            a[r][c]=input('''8. ¿Quién esculpió la estatua ecuestre de Alfonso XII (1922) 
    situada en el parque del Retiro en Madrid?  ''')
        if c==8:
            a[r][c]=input('9. ¿En qué ciudad se encuentra "El David" de Miguel Ángel?  ')
        if c==9:
            a[r][c]=input('10. ¿En qué movimiento cultural se encuentra Vermeer? ')
        if c==10:
            a[r][c]=input('11. ¿En qué ciudad se encuentra el lienzo "El entierro del conde de Orgaz"?  ')
        if c==11:
            a[r][c]=input('12. ¿Dónde se encuentra el Castillo Lichtenstein?  ')
        if c==12:
            a[r][c]=input('13. ¿Dónde se encuentra el Capricho de Gaudí?  ')
        if c==13:
            a[r][c]=input('14. ¿Qué pintor ilustró con imágenes el Quijote?  ')
        if c==14:
            a[r][c]=input('15. ¿Qué tipo de construcción era el Coliseo de Roma?  ')
        if c==15:
            a[r][c]=input('''16. ¿En qué museo se encuentra "Judit en el banquete
    de Holofernes" de Rembrandt?  ''')
        if c==16:
            a[r][c]=input('17. ¿Quién fue el escultor del "Discóbolo"?  ')
        if c==17:
            a[r][c]=input('18. ¿Dónde se encuentran los girasoles en "Los Girasoles" de Van Gogh?  ')
        if c==18:
            a[r][c]=input('19. ¿En qué movimiento cultural se encuentra Rubens?  ')
        if c==19:
            a[r][c]=input('20. ¿En qué museo se encuentra "La Vida de María de Médicis" de Rubens? ')
        if c==20:
            a[r][c]=input('''21. ¿Qué artista recibió el encargo del gobierno español 
    para pintar el bombardeo de Guernica?  ''')
        if c==21:
            a[r][c]=input('22. ¿De qué estilo arquitectónico es la catedral de Barcelona?  ')
        if c==22:
            a[r][c]=input('23. ¿En qué movimiento cultural se encuentra Tizziano?  ')
        if c==23:
            a[r][c]=input('24. ¿Cómo se llama la torre más famosa de la catedral de Valencia?  ')
        if c==24:
            a[r][c]=input('25. ¿Dónde se encuentra el "Gran Buda de Ushiku"? ')
        if c==25:
            a[r][c]=input('26. ¿Quién pintó "Las Tres Gracias"?  ')
        if c==26:
            a[r][c]=input('27. ¿Quién pintó "Las 3 Edades del Hombre"?  ')
        if c==27:
            a[r][c]=input('28. ¿Qué artista diseñó la Plaza Mayor de Salamanca?  ')
        if c==28:
            a[r][c]=input('29. ¿Dónde se encuentra el Museo del Prado?  ')
        if c==29:
            a[r][c]=input('30. ¿Dónde se encuentra la Estatua de la Libertad?  ')
        if c==30:
            a[r][c]=input('31. ¿En qué movimiento cultural se encuentra Eugéne Delacroix?  ')
        if c==31:
            a[r][c]=input('32. ¿Qué artista pintó "El Diluvio Universal"?  ')
        if c==32:
            a[r][c]=input('33. ¿En qué movimiento cultural se encuentra Charles Garnier?  ')
        if c==33:
            a[r][c]=input('''34. ¿En qué museo se encuentra "Carlos V en la 
    batalla de Mühlberg" de Tiziano?  ''')
        if c==34:
            a[r][c]=input('35. ¿En qué lugar se encuentra la Basílica de San Marcos?  ')
        if c==35:
            a[r][c]=input('36. ¿De qué estilo arquitectónico es la Sagrada Familia de Barcelona? ')
        if c==36:
            a[r][c]=input('37. ¿En dónde se encuentra la Acrópolis? ')
        if c==37:
            a[r][c]=input('38. ¿En qué ciudad se encuentra el Museo de Guggenheim? ')
        if c==38:
            a[r][c]=input('39. ¿En qué movimiento cultural se encuentra Joan Miró?  ')
        if c==39:
            a[r][c]=input('40. ¿En qué movimiento cultural se encuentra Botticelli? ')
        if c==40:
            a[r][c]=input('41. ¿De qué estilo arquitectónico es la catedral de Santiago de Compostela?  ')
        if c==41:
            a[r][c]=input('42. ¿Quién esculpió "La Piedad"? ')
        if c==42:
            a[r][c]=input('''43. ¿En qué museo se encuentra "El caballero de la
    mano en el pecho" de El Greco?  ''')
        if c==43:
            a[r][c]=input('44. ¿En qué lugar se encuentra el Palacio de Windsor?  ')
        if c==44:
            a[r][c]=input('45. ¿De qué estilo arquitectónico es la Catedral de Milán?  ')
        if c==45:
            a[r][c]=input('46. ¿De qué estilo arquitectónico es la Fontana de Trevi?  ')
        if c==46:
            a[r][c]=input('''47. El Monte Rushmore representa los primeros años de Historia
    de los Estados Unidos con las cabezas de cuatro presidentes 
    de los Estados Unidos ¿dónde se encuentra?  ''')
        if c==47:
            a[r][c]=input('48. ¿Quién diseño el "Parque Güell" declarado patrimonio de la Humanidad?  ')
        if c==48:
            a[r][c]=input('49. ¿De qué estilo arquitectónico es la Fachada de la Universidad de Salamanca?  ')
        if c==49:
            a[r][c]=input('50. "El Pensador" es una escultura de:  ')
        
        
        
        
        

