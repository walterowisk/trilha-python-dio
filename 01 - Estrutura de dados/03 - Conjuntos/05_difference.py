# Tudo que está em um conjunto e não está no outro
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado) # {1}

resultado = conjunto_b.difference(conjunto_a)
print(resultado) # {4}
