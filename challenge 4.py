import random

perguntas = ["Como me chamo?", "Que escola frequentei?"]

utilizador = input("Responde correctamente as perguntas: ")
pc= random.choice(perguntas)

if pc == perguntas[0]:
    if utilizador == "Emanuel":
        print(f"Resposta correcta, Foi adicionado 2500 euros a sua banca")
    elif utilizador == "Eped":
        print(f"Resposta correcta, Foi adicionado mais 2500 a sua banca")

    else:
        print(f"Resposta errada , acabou de perder tudo o que tem!")
