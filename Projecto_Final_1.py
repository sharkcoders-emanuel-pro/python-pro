#Calculadora

#UI
# 1) Calculos aritemeticos - Soma , subtraçao , divisao, multiplicaçao , resto, potenciaçao
# 2) Calculos Area
# 3) Caluclos Volumes
# 4) Sair

#from math import pi

#def clear():
    #for _ in range(3):
        #print("")

#def sum(n1,n2):
    #return n1 + n2

#def sub(n1,n2):
    #return n1 - n2


#def mult(n1,n2):
    #return n1 * n2


#def div(n1,n2):
    #return n1 / n2

#def pow(n1,n2):
    #return n1 ** n2

#def resto(n1,n2):
    #return n1 % n2

#def area_retangulo(largura, comprimento):
    #return largura * comprimento

#def area_circulo(raio):
    #return pi *(raio ** 2)

#def volume_prisma(base, altura):
    #return base * altura

#def volume_cilindro(raio, altura):
    #return pi * (raio ** 2) * altura

from tools import *
#import tools as t



# Programa

def main_menu():
    print(" - Calculadora XPTO - ")
    print("1 - Calculos Aritemeticos;")
    print("2 - Calculos Areas;")
    print("3 - Calculos Volumes;")
    print("4 - Sair;")
    option = int(input("\n> "))
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
            print("5 - Potenciação;")
            print("6 - resto;")
            option_arithemetic = int(input("\n> "))

            # Menu Aritemetico
            if option_arithemetic == 1:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A soma dos valores é de: {sum(n1, n2)}")
                input()
                clear()

            elif option_arithemetic == 2:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A Subtração dos valores é de: {sub(n1, n2)}")
                input()
                clear()

            elif option_arithemetic == 3:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A Multiplicação dos valores é de: {mult(n1, n2)}")
                input()
                clear()

            elif option_arithemetic == 4:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A Divisão dos valores é de: {div(n1, n2)}")
                input()
                clear()

            elif option_arithemetic == 5:
                n1 = float(input("Insira aqui o primeiro valor:  "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"O numero Potenciado é de: {pow(n1, n2)}")
                input()
                clear()

            elif option_arithemetic == 6:
                n1 = float(input("Insira aqui o primeiro valor:  "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"O Resto do Numero é de: {resto(n1, n2)}")
                input()
                clear()


            else:
                print(f"Opçao Invalida , tente outra vez!")

        elif option == 2:
            option_area = 0
            print("1 - Área do Retangulo;")
            print("2 - Área do Circulo;")
            option_area = int(input("\n> "))

            if option_area == 1:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"A Área do retangulo é de: {area_retangulo(n1, n2)}")
                input()
                clear()

            elif option_area == 2:
                n1 = float(input("Insira aqui o primeiro valor: "))
                print(f"A Área do Circulo é de: {area_circulo(n1)}")
                input()
                clear()

            else:
                print(f"Opçao Invalida , Tente Novamente!")

        elif option == 3:
            option_volume = 0
            print("1 - volume_prisma;")
            print("2 - volume_cilindro;")
            option_volume = int(input("\n> "))

            if option_volume == 1:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"O Volume do Prisma é de: {volume_prisma(n1, n2)}")
                input()
                clear()

            elif option_volume == 2:
                n1 = float(input("Insira aqui o primeiro valor: "))
                n2 = float(input("Insira aqui o segundo valor: "))
                print(f"O Volume do Cilindro é de: {volume_cilindro(n1, n2)}")
                input()
                clear()

            else:
                print(f"Opção Invalida , Tente Novamente!")
if __name__ == '__main__':
    main()









