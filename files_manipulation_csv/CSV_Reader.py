import csv

"""

    Leitura em CSV

"""

# Leitura simples com csv.reader (apresenta o conteudo completo)
# with open('pessoas.csv', newline='', encoding='utf-8') as ficheiro:
#     leitor = csv.reader(ficheiro, delimiter=';')
#     for linha in leitor:
#         print(linha)

print("\n")

# Leitura simples com csv.reader (apresenta o canteúdo sem estar como lista)

# with open('pessoas.csv', newline='', encoding='utf-8') as ficheiro:
#     leitor = csv.reader(ficheiro, delimiter=';')
#     for linha in leitor:
#         print(linha[0], linha[1], linha[2]) # os indices representam as colunas

print("\n")

# Leitura simples com csv.reader (apresenta o canteúdo sem estar como lista,ignorando o cabeçalho)

# with open('pessoas.csv', newline='', encoding='utf-8') as ficheiro:
#     leitor = csv.reader(ficheiro, delimiter=';')
#     next(leitor) # ignora o cabeçalho
#     for linha in leitor:
#         print(linha[0], linha[1], linha[2]) # os indices representam as colunas



# Leitura com dicionario


# with open('pessoas.csv', newline='', encoding='utf-8') as ficheiro:
#     leitor = csv.DictReader(ficheiro, delimiter=';')
#     for linha in leitor:
#         print(linha["Nome"], linha["Idade"], linha["Profissão"])



"""

    Escrita em CSV

"""


# Escrever Listas de Listas para o Csv

# dados_lista = [["Nome", "Idade","Profissão"],
#                ["Diana",  "28", "Designer"],
#                 ["Diogo",  "29", "Arquitecto"]]
#
# with open("escrita_lista.csv","w", newline="", encoding="utf-8") as ficheiro:
#     escritor = csv.writer(ficheiro, delimiter=";")
#     escritor.writerows(dados_lista)


# Escrever dicionarios para o csv

# dados_dict = [
#     {"Nome":"Fábio", "Idade":40, "Profissão":"Advogado"},
#     {"Nome":"Aberto", "Idade":45, "Profissão":"Camionista"},
#     {"Nome":"José", "Idade":35, "Profissão":"Carteiro"}
# ]
#
# with open("escrita_dict.csv", "w", newline="", encoding="utf-8") as fichero:
#     colunas = ["Nome", "Idade", "Profissão"]
#     escritor = csv.DictWriter(fichero, fieldnames=colunas, delimiter=";")
#     escritor.writeheader()
#     escritor.writerows(dados_dict)


"""
    Atualizar em CSV
    
"""


linhas = []
with open("pessoas.csv", newline='', encoding='utf-8') as ficheiro:
    leitor = csv.DictReader(ficheiro, delimiter=';')
    for linha in leitor:
        if linha["Nome"] == "Ana":
            linha["Idade"] = "26"
        linhas.append(linha)


with open('pessoas.csv', 'w', newline='', encoding='utf-8') as ficheiro:
    campos = ["Nome", "Idade", "Profissão"]
    escritor = csv.DictWriter(ficheiro, fieldnames=campos, delimiter=';')
    escritor.writeheader()
    escritor.writerows(linhas)

"""
    Eliminar em CSV

"""


linhas = []

with open('pessoas.csv', newline='', encoding='utf-8') as ficheiro:
    leitor = csv.DictReader(ficheiro, delimiter=';')
    for linha in leitor:
        if linha["Nome"] != "Bruno":
            linhas.append(linha)


with open('pessoas.csv', 'w', newline='', encoding='utf-8') as ficheiro:
    campos = ["Nome", "Idade", "Profissão"]
    escritor = csv.DictWriter(ficheiro, fieldnames=campos, delimiter=';')
    escritor.writeheader()
    escritor.writerows(linhas)