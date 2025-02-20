lista_paises = ["Portugal", "Espanha", "França", "Italia"]

user = input("Indica qual este pais na Europa: ").title()

if user in lista_paises:
    print("Portugal esta na lista")
elif user in lista_paises:
    print("Espanha esta na lista")
elif user in lista_paises:
    print("França esta na lista")
elif user in lista_paises:
    print("Italia esta na lista")
else:
    print(f"Nao há esse pais na lista")