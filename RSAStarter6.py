from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long

# Función para leer la clave privada desde el archivo
def leer_clave_privada(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()
        N = int(lineas[0].strip().split('=')[1])
        d = int(lineas[1].strip().split('=')[1])
    return N, d

# Leer la clave privada desde el archivo
ruta_archivo = 'C:\\Users\\denni\\Documents\\Octavo Semestre\\Cripto\\retos\\private.key'
N, d = leer_clave_privada(ruta_archivo)

# Mensaje que queremos firmar
mensaje = "crypto{Immut4ble_m3ssag1ng}"

# Calcular el hash SHA256 del mensaje
hash_mensaje = SHA256.new(mensaje.encode()).digest()

# Convertir el hash a un número
hash_numero = bytes_to_long(hash_mensaje)

# Firmar el hash del mensaje utilizando la clave privada
firma = pow(hash_numero, d, N)

# Mostrar la firma
print(f"Firma: {firma}")

