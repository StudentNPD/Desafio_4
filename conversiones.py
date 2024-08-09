# Desafio Conversión 
# sys.argv -> Sol, Peso Argentino, Dólar Americano 
# ● a Sol peruano: 0.0046
# ● a Peso Argentino: 0.093
# ● a Dólar Americano: 0.00013

# python conversiones.py 0.0046 0.093 0.0013 10000
# Los 10000 pesos equivalen a:
# 46.0 Soles
# 930.0 Pesos Argentinos
# 13.0 Dólares

import sys

# validacion del ingreso del archivo como argumento
if len(sys.argv) <5:
    print('Recuerda que debes ingresar las siguientes tasas: \nSoles \nPesos Argentinos \nDolares \nValor a convertir(CLP)')
    exit()

# Declarando variables
sol = float(sys.argv[1])
argentino = float(sys.argv[2])
americano = float(sys.argv[3])
chileno =   float(sys.argv[4])

for i in range(1):
    print(f"Los {chileno} equivalen a:")
    # Conversión de tasas
    conversion1 = sol * chileno
    conversion2 = argentino * chileno
    conversion3 = americano * chileno
    # Mostrar Conversión a Soles, Arg y Dolares
    print(f"{conversion1} Soles")
    print(f"{conversion2} Peso Argentino")
    print(f"{conversion3} Dolares")
    