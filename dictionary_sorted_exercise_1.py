products = {'Camarão': 24,'Frango': 23,'Leite': 8,'Peixe': 20,'Soja': 58}
print(sorted(products))

print("\n")

for x in sorted(products.items()):
    print(f"O {x[0]} tem {x[1]} de proteina a cada 100G.")







