import sys

with open(sys.argv[1]) as file:
    texto=file.read()
    #caracteres distintos
    caract_distintos = len(set(texto))



    #separando palabras
    arreglo_texto=texto.split(" ")
    palabras_distintas=len(set(arreglo_texto))
    
    print(f"El número de caracteres distintos es: {caract_distintos}")
    print(f"El número de palabras distintas es: {palabras_distintas}")        
    
