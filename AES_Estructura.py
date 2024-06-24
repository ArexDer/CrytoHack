#EJERCIO DE UNA ESTRUCTURA AES PASAR DE MATRIZ A BITS

def bytes2matrix(texto):
    #Convierte un array de 16 bytes en una matriz 4x4. 
    # Crea una lista de listas donde cada sublista contiene 4 elementos consecutivos del texto
    return [list(texto[i:i+4]) for i in range(0, len(texto), 4)]

def matrix2bytes(matriz):
    # Convierte una matriz 4x4 en un array de 16 bytes.
    texto = ''
    # Itera sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Itera sobre cada elemento de la fila (cada elemento es un número entero)
        for j in range(4):
            # Convierte el número entero en un carácter y lo concatena a la cadena 'texto'
            texto += chr(matriz[i][j])
    return texto

# Ejemplo de una matriz 4x4
matriz = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# Llama a la función matrix2bytes para convertir la matriz en una cadena de bytes y la imprime
print(matrix2bytes(matriz))
