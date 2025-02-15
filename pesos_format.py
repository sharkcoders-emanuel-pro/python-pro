maior = menor = 0


for n in range(1,6):
    num = int(input(f" Entre com o {n}º peso: "))
    if n == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num


print (" O Número maior é:", maior)
print (" O Número maior é:", menor)
