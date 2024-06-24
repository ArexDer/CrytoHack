#CODIGO EN LA CREACION DE CUENTA, DESCIFRAR EL MENSAJE.
#---Este codigo analiza su entrada y empieza a desplazar las letras,
#---con esto nos arroja los 25 resultados y vemos cual es el correcto.
#---en este caso es el 14.(14 desplazamientos de letras)

def cifrado_Cesar(mensajeEntrada, desplazamiento):
    resultado = ""
    for char in mensajeEntrada:
        # Si el carácter es una letra
        if char.isalpha():
            # Verificar si es mayúscula o minúscula
            ascii_M_o_m = 65 if char.isupper() else 97
            # Desplazar el carácter y ajustar dentro del rango alfabético
            resultado += chr((ord(char) - ascii_M_o_m - desplazamiento) % 26 + ascii_M_o_m)
        else:
            # Si no es una letra, agregar el carácter tal cual
            resultado += char
    return resultado

# Mensaje cifrado
cipher_mensajeEntrada = "WBGSQH ZWOF OKYKOFR OTTOWF"

# Probar con un desplazamiento de 3 (desplazamiento de César)
desplazamiento = 3
mensaje_Descifrado = cifrado_Cesar(cipher_mensajeEntrada, desplazamiento)
print(f"Desplazamiento {desplazamiento}: {mensaje_Descifrado}")

# Probar con otros desplazamientos si es necesario
for desplazamiento in range(1, 26):
    mensaje_Descifrado = cifrado_Cesar(cipher_mensajeEntrada, desplazamiento)
    print(f"Desplazamiento {desplazamiento}: {mensaje_Descifrado}")
