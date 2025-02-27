valores = [-5,7,1,0,10,100,33,2]
quadrado = []

for v in valores:
    quadrado.append(v**2)
print(f"Os numeros elevados ao quadrado sao {quadrado}")

#list comprehension

quadrado = [v ** 2 for v in valores]
print(quadrado)