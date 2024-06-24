#Algoritmo Extendido de Euclides para encontrar el máximo común divisor
def extendido_mcd(a, b):

    if a == 0:
        return (b, 0, 1)
    else:
        #Si a no es 0, llama recursivamente a sí misma con b % a
        g, y, x = extendido_mcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Calcula el inverso modular de g módulo p usando el Algoritmo Extendido de Euclides.
def mod_inversa(g, p):
    g = g % p
    gcd, x, y = extendido_mcd(g, p)
    if gcd != 1:
        raise Exception('El inverso modular no existe')
    else:
        return x % p

p = 991
g = 209
d = mod_inversa(g, p)
print(f"El inverso de {g} en módulo {p} es: {d}")