def sumar():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = a + b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")

def restar():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = a - b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


def multiplicar():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = a * b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


def dividir():
    try:
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador: "))
        if b == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = a / b
            print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


def potencia():
    try:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = base ** exponente
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


import math

def raiz_cuadrada():
    try:
        numero = float(input("Ingrese el n�mero: "))
        if numero < 0:
            print("Error: No se puede calcular la ra�z cuadrada de un n�mero negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"Resultado: {resultado}")
    except ValueError: 
        print("Error: Ingrese un valor num�rico v�lido.")


def modulo():
    try:
        numero = float(input("Ingrese el n�mero: "))
        resultado = abs(numero)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un valor num�rico v�lido.")

      
def redondear():
    try:
        numero = float(input("Ingrese el n�mero: "))
        resultado = round(numero)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un valor num�rico v�lido.")


def menor():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = min(a, b)
        print(f"El menor es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


def mayor():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = max(a, b)
        print(f"El mayor es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")


def promedio():
    try:
        a = float(input("Ingrese el primer n�mero: "))
        b = float(input("Ingrese el segundo n�mero: "))
        resultado = (a + b) / 2
        print(f"El promedio es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores num�ricos v�lidos.")



def factorial():
    try:
        numero = int(input("Ingrese un n�mero entero no negativo: "))
        if numero < 0:
            print("Error: No se puede calcular el factorial de un n�mero negativo.")
        else:
            resultado = math.factorial(numero)
            print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un n�mero entero v�lido.")





def mostrar_menu():
    print("=" * 40)
    print("  Bienvenido al sistema de operaciones")
    print("=" * 40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=" * 40)

def main():

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opci�n: ")
        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            print("Programa finalizado.")
            continuar = False
        else:
            print("Opci�n inv�lida")

if __name__ == "__main__":
    main()




