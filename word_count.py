import sys

with open(sys.argv[1]) as file:
    texto=file.read()
    #caracteres distintos
    caract_distintos = len(set(texto))

    
    