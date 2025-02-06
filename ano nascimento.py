from datetime import date

ano_nascimento = int(input("Em que ano nasceu?: "))

idade = date.today().year - ano_nascimento

if idade < 18:
    print(f"ainda nao tens idade para o alistamento")
elif idade >= 18 and idade <= 25:
    print(f"Está no prazo para o alistamento")
elif idade > 25:
    print(f"Já lhe passou o prazo para alistamento")

