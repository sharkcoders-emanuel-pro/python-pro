nota1 = nota2 = nota3 = 0

try:
    print("Inserir apenas Numeros Interos.")
    nota1 = int(input("intruduza aqui a sua nota: "))
    nota2 = int(input("intruduza aqui a sua nota: "))
    nota3 = int(input("intruduza aqui a sua nota: "))

except (ValueError,TypeError):
    print('Inseriste um número invalido, tenta outra vez o Try.')



media_notas = (nota1 + nota2 + nota3) / 3

print(f"O aluno teve uma média de : {media_notas}")