import base64

# Cadena hexadecimal proporcionada
candena_hexadecimal = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convertir la cadena hexadecimal a bytes
bytes_data = bytes.fromhex(candena_hexadecimal)

# Codificar los bytes en Base64
base64_encoded = base64.b64encode(bytes_data)

# Convertir el resultado de bytes a una cadena
flag = base64_encoded.decode('utf-8')

# Mostrar la bandera
print("La bandera es:", flag)
