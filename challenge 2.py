kWh = float(input("introdusa a sua quantidade: "))
tipo_habitacao = input("introduza sua tipologia: ")

if tipo_habitacao == "R" or tipo_habitacao == "r":
    if kWh <= 500:
        kWh = kWh * 0.40
        print(f"{kWh}")
    if kWh > 500:
        kWh = kWh * 0.65
        print(f"{kWh}")

if tipo_habitacao == "C" or tipo_habitacao == "c":
    if kWh <= 1000:
        kWh = kWh * 0.55
        print(f"{kWh}")
    if kWh > 1000:
        kWh = kWh * 0.60
        print(f"{kWh}")

if tipo_habitacao == "I" or tipo_habitacao == "i":
    if kWh <= 5000:
        kWh = kWh * 0.55
        print(f"{kWh}")
    if kWh > 5000:
        kWh = kWh * 0.60
        print(f"{kWh}")

