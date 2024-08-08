import sys


# validacion del ingreso del archivo como argumento
if len(sys.argv) <2:
    print('Por favor, ingresa un archivo como argumento')
    exit()


with open(sys.argv[1]) as file:
    texto=file.read()
    #caracteres distintos
    caract_distintos = len(set(texto))

    #elimina "," del texto
    texto=texto.replace(","," ")
    #elimina "." del texto
    texto=texto.replace("."," ")

    #separando palabras
    arreglo_texto=texto.split(" ")
    palabras_distintas=len(set(arreglo_texto))
    
    print(f"El número de caracteres distintos es: {caract_distintos}")
    print(f"El número de palabras distintas es: {palabras_distintas}")        
    
