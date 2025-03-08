from random import randint

def sort_list(size, first_value, last_value):
    tmp = []
    for _ in range(size):
        tmp.append(randint(first_value,last_value))
    return tmp

def sum_list(list):
    sum = 0
    for i in list:
        if (i % 2) == 0:
            sum += i
    return sum


# novo ficheiro

while True:
    size = int(input("introduza aqui o Tamanho: "))
    first_value = int(input("introduza aqui o primeiro valor: "))
    last_value = int(input("introduza aqui o ultimo valor: "))
    my_list = sort_list(size, first_value, last_value)
    print(my_list)
    print(sum_list(my_list))









