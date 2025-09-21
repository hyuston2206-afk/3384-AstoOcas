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


import random


def numero_aleatorio():
    try:
        minimo = int(input("Ingrese el valor m�nimo: "))
        maximo = int(input("Ingrese el valor m�ximo: "))
        if minimo > maximo:
            print("Error: El m�nimo no puede ser mayor que el m�ximo.")
        else:
            resultado = random.randint(minimo, maximo)
            print(f"N�mero aleatorio generado: {resultado}")
    except ValueError:
        print("Error: Ingrese n�meros enteros v�lidos.")


def convertir_grados():
    try:
        opcion = input("�Desea convertir a (C)elsius o (F)ahrenheit?: ").strip().upper()
        temperatura = float(input("Ingrese la temperatura: "))
        
        if opcion == "C":
            resultado = (temperatura - 32) * 5 / 9
            print(f"{temperatura}�F son {resultado:.2f}�C")
        elif opcion == "F":
            resultado = (temperatura * 9 / 5) + 32
            print(f"{temperatura}�C son {resultado:.2f}�F")
        else:
            print("Opci�n inv�lida. Use 'C' o 'F'.")
    except ValueError:
        print("Error: Ingrese una temperatura v�lida.")



def mostrar_menu():
    print("\n Bienvenido al sistema de operaciones matem�ticas ")
    print("Seleccione una opci�n:")
    print("1) Factorial")
    print("2) N�mero aleatorio")
    print("3) Conversi�n de grados")
    print("4) Salir")

    try:
        opcion = int(input("Ingrese el n�mero de la opci�n: "))
        if opcion == 1:
            numero = int(input("Ingrese un n�mero entero: "))
            factorial(numero)
        elif opcion == 2:
            numero_aleatorio()
        elif opcion == 3:
            convertir_grados()
        elif opcion == 4:
            print("�Gracias por usar el sistema! ")
        else:
            print("Opci�n inv�lida. Por favor, ingrese un n�mero entre 1 y 4.")
    except ValueError:
        print("Error: Ingrese un n�mero v�lido.")





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




