import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elije un numero del 1 al 100 :"))
    oportunidad = 1
    while numero_elegido != numero_aleatorio:
        oportunidad += 1
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_elegido = int(input("Elije otro numero  :"))
    print("Ganaste en la oportunidad numero " + str(oportunidad))


if __name__ == "__main__":
    run()