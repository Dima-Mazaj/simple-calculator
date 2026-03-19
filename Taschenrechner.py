def rechner():
    z1 = float(input("Gebe die erste Zahl ein: "))
    op = input("Welche Rechenoperation? (+) (-) (*) oder (/) ")
    z2 = float(input("Gebe die zweite Zahl ein: "))

    if op == "+":
        return z1 + z2
    elif op == "-":
        return z1 - z2
    elif op == "*":
        return z1 * z2
    elif op == "/":
        return z1 / z2
    else:
        print("Fehler!")

ergebnis = rechner()
print(ergebnis)

