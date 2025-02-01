from random import randint

pc = randint(0,5)

print(pc)

numero = int(input("qual foi o numero que o computador deu?: "))



if numero == pc:
    print(f"parabens voces acertou")

else:
    print(f"tente novamente")




