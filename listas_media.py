quantidade = int(input("Quantas notas deseja inserir? "))

notas =[]
soma = 0

for i in range(quantidade):
    nota = float(input(f"Insira a nota {i + 1}: "))
    soma += nota
    notas.append(nota)

print(f"Média: {soma / len(notas)}")
