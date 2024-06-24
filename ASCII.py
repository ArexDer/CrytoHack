# Lista de números enteros
numeros_ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convertir cada número a su carácter ASCII correspondiente
flag = ''.join(chr(num) for num in numeros_ascii)

# Mostrar la bandera
print("La bandera es:", flag)
