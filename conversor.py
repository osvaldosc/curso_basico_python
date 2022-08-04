pesos = input("Cuantos pesos tienes?: ")
pesos = float(pesos)
valor_dolar = 20
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares +" dolares")
