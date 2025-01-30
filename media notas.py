nota1 = float(input("intruduza aqui a sua nota: "))
nota2 = float(input("intruduza aqui a sua nota: "))

media_notas = (nota1 + nota2) / 2

print(f"{media_notas}")

if media_notas > 60:
    print("Parabéns! Foi Aprovado")

else:
    print("Infelizmente foi Reprovado")