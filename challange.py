from pydoc import describe

nome_funcionario = input("Nome do funcionario: ")
horas_trabalhadas = float(input("horas trabalhadas: "))
numero_dependetes = int(input("numero de dependetes: "))

salario_hora = horas_trabalhadas * (12)
salario_dependetes = numero_dependetes * (40)

salario_bruto = salario_hora + salario_dependetes

desconto_inss = salario_bruto * (8.5 / 100)
desconto_irs = salario_bruto * (5 / 100)

salario_liquido = salario_bruto - desconto_irs - desconto_inss

print(f"{salario_bruto}€")
print(f"{desconto_inss:.2f}€")
print(f"{desconto_irs:.2f}€")

print(f"O nome do funcionario é: {nome_funcionario}"
      f", o seu salario bruto é de : {salario_bruto}€"
      f", o desconto para inss foi de : {desconto_inss:.2f}€"
      f", irs de : {desconto_irs:.2f}€,"
      f" logo o seu salario liquido é de: {salario_liquido}€ ")


