ordenado_funcionario = int(input("Qual o seu Ordenado: "))

if ordenado_funcionario < 500:
    reajuste = ordenado_funcionario * (15/100)
    print(f"O seu ordenado passara para {ordenado_funcionario + reajuste} ")
elif ordenado_funcionario >= 500 and ordenado_funcionario <= 1000:
    reajuste = ordenado_funcionario * (10/100)
    print(f"O seu ordenado passara para {ordenado_funcionario + reajuste}")
elif ordenado_funcionario > 1000:
    reajuste = ordenado_funcionario * (5/100)
    print(f"O seu ordenado passara para {ordenado_funcionario + reajuste}")

else:
    print(f"valor invalido")

