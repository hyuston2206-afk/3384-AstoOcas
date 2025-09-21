def sumar():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a + b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def restar():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a - b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


def multiplicar():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a * b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


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
        print("Error: Ingrese valores numéricos válidos.")


def potencia():
    try:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = base ** exponente
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


import math

def raiz_cuadrada():
    try:
        numero = float(input("Ingrese el número: "))
        if numero < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"Resultado: {resultado}")
    except ValueError: 
        print("Error: Ingrese un valor numérico válido.")


def modulo():
    try:
        numero = float(input("Ingrese el número: "))
        resultado = abs(numero)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

      
def redondear():
    try:
        numero = float(input("Ingrese el número: "))
        resultado = round(numero)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")


def menor():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = min(a, b)
        print(f"El menor es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


def mayor():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = max(a, b)
        print(f"El mayor es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


def promedio():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = (a + b) / 2
        print(f"El promedio es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")



def factorial():
    try:
        numero = int(input("Ingrese un número entero no negativo: "))
        if numero < 0:
            print("Error: No se puede calcular el factorial de un número negativo.")
        else:
            resultado = math.factorial(numero)
            print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingrese un número entero válido.")





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
        opcion = input("Seleccione una opción: ")
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
            print("Opción inválida")

if __name__ == "__main__":
    main()




