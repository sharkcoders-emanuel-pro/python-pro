carro = input("Qual o nome do automovel?: ")
preco = float (input ("qual o valor do carro?: "))

impostos = preco * (21/100)
revendedor = (preco * (28/100)) + impostos

precofinal = preco + impostos + revendedor

print(f"O carro {carro} tem como preco final {precofinal:.2f}€")
