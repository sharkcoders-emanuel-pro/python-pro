from random import randint

pc = randint(1, 100)

print(pc)

counter = 0

while True:

    user = int(input("(1, 100)> "))

    if user == pc:
        print("o numero é igual")
        counter += 1
        break

    elif user > pc:
        print("O numero é menor")
        counter += 1

    elif user < pc:
        print("O numero é maior")
        counter += 1


print(f"Foram necessarias {counter} jogadas para vencer!")