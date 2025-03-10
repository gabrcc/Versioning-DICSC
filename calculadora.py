import sys 
from decimal import Decimal

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def main():
    print("\nCalculadora basica - Version 1.0")
    while True:
        
        print("\n1. Suma")
        print("2. Resta")
        print("3. Exit")

        opcion = input("\nIngrese el numero de la operacion a realizar: ")
        if opcion == "3":
            print("EXIT")
            sys.exit()

        if opcion not in ["1", "2"]:
            print("Opcion invalida")
            continue
        
        try:
            n1 = Decimal(input("\nIngrese el primer numero: "))
            n2 = Decimal(input("Ingrese el segundo numero: "))
        except ValueError:
            print("\nEntrada invalida")
            continue
        if opcion == "1":
            print(f"\n******Resultado: {suma(n1, n2)}******")
        elif opcion == "2":
            print(f"\n******Resultado: {resta(n1, n2)}******")   

if __name__ == "__main__":
    main()            