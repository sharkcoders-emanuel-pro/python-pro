numero_inicial = int(input("introduza aqui o seu numero inicial: "))
numero_final = int(input("introduza aqui o seu numero final: "))
ver = input("par ou impar: ")

for i in range(numero_inicial , numero_final+1):
    if (i % 2) == 0 and ver == 'par':
        print(i)
    elif (i % 2) != 0 and ver == 'impar':
        print(i)
