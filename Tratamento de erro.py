try:
    n1 = int(input('Numero1:'))
    n2 = int(input('Numero1:'))
    r= n1/n2

except (ValueError, TypeError):
    print('Problemas com os dadaos de entrada')

except ZeroDivisionError:
    print('Não divisivel por Zero')

except KeyboardInterrupt:
    print('O programa foi Interrompido')

else:
    print(f"O resultado é {r:.1f}")

finally:
    print("Volte Sempre!")