import random

# Diccionario con los números de oxidación de los elementos
numeros_oxidacion = {"H": [1, -1],
                     "Li": [1], "Na": [1], "K": [1], "Rb": [1], "Cs": [1], "Fr": [1], "Ag": [1],
                     "Be": [2], "Mg": [2], "Ca": [2], "Sr": [2], "Ba": [2], "Ra": [2], "Zn": [2], "Cd": [2],
                     "Cr": [2, 3, 6],
                     "Mn": [2, 3, 4, 6, 7],
                     "Fe": [2, 3], "Co": [2, 3], "Ni": [2, 3],
                     "Cu": [1, 2], "Hg": [1, 2],
                     "Au": [1, 3],
                     "Pd": [2, 4], "Pt": [2, 4], "Ti": [2, 4], "Sn": [2, 4], "Pb": [2, 4],
                     "B": [3], "Al": [3],
                     "C": [2, 4, -2, -4], "Si": [2, 4, -2, -4],
                     "N": [1, 2, 3, 4, 5, -3],
                     "P": [3, 5, -3], "As": [3, 5, -3], "Sb": [3, 5, -3],
                     "O": [-2],
                     "S": [4, 6, -2], "Se": [4, 6, -2], "Te": [4, 6, -2],
                     "F": [-1],
                     "Cl": [1, 3, 5, 7, -1], "Br": [1, 3, 5, 7, -1], "I": [1, 3, 5, 7, -1]
                    }

# Contadores
total = 0
aciertos = 0
fallos = 0
preguntas_realizadas = []

while True:
    # Selecciona un elemento al azar
    elemento = random.choice(list(numeros_oxidacion.keys()))
    while elemento in preguntas_realizadas:
        elemento = random.choice(list(numeros_oxidacion.keys()))
    preguntas_realizadas.append(elemento)
    
    print('\n'+"¿Cuáles son los números de oxidación del elemento " + elemento + "?")
    respuesta = input()
    # Convierte la respuesta en una lista de enteros
    respuesta = [int(num) if num[0] != '-' else -int(num[1:]) for num in respuesta.split()]
    correcta = numeros_oxidacion[elemento]
    
    # Aumenta el contador de preguntas
    total += 1
    
    if respuesta == correcta:
        print("¡Correcto!")
        # Aumenta el contador de aciertos
        aciertos += 1
    else:
        print("Incorrecto. La respuesta correcta es: ", end='')
        for num in correcta:
            if num < 0:
                print("(" + str(num) + ")", end=' ')
            else:
                print(num, end=' ')
        print()
        # Aumenta el contador de fallos
        fallos += 1
        
    print("\nEstadísticas hasta ahora:")
    print("Total preguntas:", total)
    print("Aciertos:", aciertos)
    print("Fallos:", fallos)
