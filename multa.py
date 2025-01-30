velocidade = int(input("introduza a sua velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 2
    print(f"{multa}€")

else:
    print("boa viagem")