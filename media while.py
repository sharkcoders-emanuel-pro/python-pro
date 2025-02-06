a_executar = 's'

while a_executar != 'n' :


    nome = input("insira o nome do aluno: ")
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >0 and media < 9.5:
        print (f"O {nome} teve Negativa, com uma média de: {media:.2f}")

    elif media >= 9.5 and media < 15:
        print (f"O {nome} teve Positiva, com uma média de: {media:.2f}")

    elif media >15 and media < 20:
        print (f"O {nome} teve Exelente, com uma média de: {media:.2f}")

    else:
        print("O valor calculado é Invalido")

    a_executar = input("Deseja continuar (s/n)? ").lower()