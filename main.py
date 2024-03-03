meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "fuera del teclado" ,
            "BOOMER": "muy viejo y no quiere entender a los jovenes" ,  
            "BASADO": "Tiene a su disposicion toda la verdad",
            "CREEPY": "tenebroso o de miedo",
            " GG" : "Buen juego" ,  
            " NT" : "buen intento" ,
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
        print (meme_dict[word] )
else:
    # ¿Qué hacer si no se encuentra la palabra?
        print ( "no se encontro la llave")
