from random import randint

lutador_a_vida = 100
lutador_b_vida = 100

while lutador_a_vida > 0 and lutador_b_vida > 0:

    # lutador A

    golpe_a = randint(10,25)
    lutador_b_vida -= golpe_a

    if lutador_b_vida < 0:
        lutador_b_vida = 0

    print(f"O Lutador A deu um soco de força {golpe_a} e a vida do lutador B foi para {lutador_b_vida}.")

    if lutador_b_vida == 0:
        print(f"O lutador A Venceu!")
        break

    # Lutador B

    golpe_b = randint(10, 25)
    lutador_a_vida -= golpe_b

    if lutador_a_vida < 0:
        lutador_a_vida = 0

    print(f"O Lutador B deu um soco de força {golpe_b} e a vida do lutador A foi para {lutador_a_vida}.")

    if lutador_a_vida == 0:
        print(f"O lutador B Venceu!")
        break


