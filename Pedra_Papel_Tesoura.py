from random import choice

opcoes = ["pedra", "papel", "tesoura"]

utilizador = input("Escolha pedra, papel ou tesoura:").lower()
while utilizador not in opcoes:
    utilizador = input("Escolha inválida! Tente novamente (pedra , papel , tesoura):").lower()

pc = choice(opcoes)
print(f"O computador escolheu: {pc}")

if utilizador == pc:
    print("Empate!")
elif (utilizador == "pedra" and pc == "tesoura") or \
     (utilizador == "tesoura" and pc == "papel") or \
     (utilizador == "papel" and pc == "pedra"):
    print("Ganhaste!")

else:
    print("Perdeste!")