from sympy import mod_inverse

# Valores dados
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calcular N
N = p * q

# Calcular la función totiente φ(N) (p−1)×(q−1)
phi_N = (p - 1) * (q - 1)

# Calcular el inverso multiplicativo modular de e modulo φ(N)
d = mod_inverse(e, phi_N)

# Imprimir la clave privada
print("Clave privada d:", d)

#**********************************#

# Valores dados para el nuevo problema
N_new = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932

# Usar pow para calcular c^d mod N de manera eficiente
m = pow(c, d, N_new)

# Imprimir el mensaje descifrado
print("Mensaje descifrado m:", m)
