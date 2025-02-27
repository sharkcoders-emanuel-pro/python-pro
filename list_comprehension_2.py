# Criar uma lista apenas com números pares

numeros = range(10)
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#

pares = [numero for numero in range(10) if numero % 2 == 0]
impares = [numero for numero in range(10) if numero % 2 != 0]
print(pares)
print(impares)