lista = [-5,7,1,0,10,100,33,2]

i = 0

while i < len(lista):
    lista[i] = lista[i] ** 2
    i += 1

for _ in lista:
    print(f"{_} ", end='')



valores = [-5,7,1,0,10,100,33,2]
quadrado = []

for v in valores:
    quadrado.append(v**2)
print(f"Os numeros elevados ao quadrado sao {quadrado}")





