#Calculadora

#UI
# 1) Calculos aritemeticos - Soma , subtraçao , divisao, multiplicaçao , resto, potenciaçao
# 2) Calculos Area
# 3) Caluclos Volumes
# 4) Sair

from math import pi

def sum(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2


def mult(n1,n2):
    return n1 * n2


def div(n1,n2):
    return n1 / n2

def area(largura, comprimento):
    return largura * comprimento

# Programa

def main_menu():
    print(" - Calculadora XPTO - ")
    print("1 - Calculos Aritemeticos;")
    print("2 - Calculos Areas;")
    print("3 - Calculos Volumes;")
    print("4 - Sair;")
    option = int(input("\n>"))
    return option


def main():

    option = 0
    while option != 4:
        option = main_menu()
        # Menu Principal
        if(option == 1):
            option_arithemetic = 0
            print("1 - Soma;")
            print("2 - Subtraçao;")
            print("3 - Multiplicaçao;")
            print("4 - Divisao;")
            option_arithemetic = int(input("\n>"))

            # Menu Aritemetico
            if(option_arithemetic == 1):
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A soma dos valores é de: {sum(n1, n2)}")

            elif (option_arithemetic == 2):
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A soma dos valores é de: {sub(n1, n2)}")

            elif (option_arithemetic == 3):
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A soma dos valores é de: {mult(n1, n2)}")

            elif (option_arithemetic == 4):
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A soma dos valores é de: {div(n1, n2)}")

            else:
                print(f"Opçao Invalida , tente outra vez!")


if __name__ == '__main__':
    main()









