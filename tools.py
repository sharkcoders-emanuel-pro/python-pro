from math import pi

def clear():
    for _ in range(10):
        print("")

def sum(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2


def mult(n1,n2):
    return n1 * n2


def div(n1,n2):
    return n1 / n2

def pow(n1,n2):
    return n1 ** n2

def resto(n1,n2):
    return n1 % n2

def area_retangulo(largura, comprimento):
    return largura * comprimento

def area_circulo(raio):
    return pi *(raio ** 2)

def volume_prisma(base, altura):
    return base * altura

def volume_cilindro(raio, altura):
    return pi * (raio ** 2) * altura