from random import randint

counter = 0

while True:

    d1 = randint(1,6)
    d2 = randint(1,6)
    if d1== 6 and d2 == 6:
        print(f"{d1} x {d2}")
        counter += 1
        break
    else:
        print(f"{d1} x {d2}" )
        counter += 1

print(f"fora preciso {counter} para obter o 6 x 6.")