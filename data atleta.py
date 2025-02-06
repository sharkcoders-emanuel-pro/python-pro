from datetime import date

ano_nascimento = int(input("Em que ano nasceu?: "))

idade = date.today().year - ano_nascimento

if idade > 0 and idade <= 9:
    print(f"Esta na classe Mirin")

elif idade >= 10 and idade <= 14 :
    print(f"Esta na classe Infantil")

elif idade >= 15 and idade <= 18:
    print(f"Esta na classe Junior")

elif idade >= 19 and idade <= 24:
    print(f"Esta na classe Senior")

elif idade > 26:
    print(f"Esta na classe de Master")