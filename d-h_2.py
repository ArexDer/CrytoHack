#Verificar si es primo
def es_primo(n):
    if n <= 1:
        return False
    #Iterar de 2 a la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factores_primos(n):
    #Primer primo es 2
    i = 2
    #Conjunto de factores primos de n declarado en vacio
    factores = set()

    while i * i <= n:
        #Si n es divisible por i, añadir i a factores
        if n % i:
            i += 1
        #Si n no es divisible por i, dividir n por i
        else:
            n //= i
            factores.add(i)

    #Si n es mayor que 1, añadir n a factores
    if n > 1:
        factores.add(n)
    return factores

def encontrar_elemento_primitivo(p):
    #Si p no es primo, retornar None
    if not es_primo(p):
        return None
    #Obtener factores primos de p-1
    factores = factores_primos(p-1)

    for g in range(2, p):
        #Si g no es un generador, probar con otro g
        for q in factores:
            if pow(g, (p-1)//q, p) == 1:
                break
        else:
            return g
    return None

p = 28151
print(encontrar_elemento_primitivo(p))