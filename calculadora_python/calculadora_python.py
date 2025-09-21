
# -*- coding: utf-8 -*-
import math
import random
from datetime import datetime

def guardar_historial(operacion, resultado):
    try:
        with open("historial.txt", "a", encoding="utf-8") as archivo:
            tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{tiempo}] {operacion}: {resultado}\n")
    except Exception as e:
        print(f"Error al guardar el historial: {e}")

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Intente de nuevo.")

def sumar():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = a + b
    print(f"Resultado: {resultado}")
    guardar_historial("Suma", resultado)

def restar():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = a - b
    print(f"Resultado: {resultado}")
    guardar_historial("Resta", resultado)

def multiplicar():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = a * b
    print(f"Resultado: {resultado}")
    guardar_historial("Multiplicacion", resultado)

def dividir():
    a = pedir_numero("Ingrese el numerador: ")
    b = pedir_numero("Ingrese el denominador: ")
    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = a / b
        print(f"Resultado: {resultado}")
        guardar_historial("Division", resultado)

def potencia():
    base = pedir_numero("Ingrese la base: ")
    exponente = pedir_numero("Ingrese el exponente: ")
    resultado = base ** exponente
    print(f"Resultado: {resultado}")
    guardar_historial("Potencia", resultado)

def raiz_cuadrada():
    numero = pedir_numero("Ingrese el numero: ")
    if numero < 0:
        print("Error: No se puede calcular la raiz cuadrada de un numero negativo.")
    else:
        resultado = math.sqrt(numero)
        print(f"Resultado: {resultado}")
        guardar_historial("Raiz cuadrada", resultado)

def modulo():
    numero = pedir_numero("Ingrese el numero: ")
    resultado = abs(numero)
    print(f"Resultado: {resultado}")
    guardar_historial("Modulo", resultado)

def redondear():
    numero = pedir_numero("Ingrese el numero: ")
    resultado = round(numero)
    print(f"Resultado: {resultado}")
    guardar_historial("Redondeo", resultado)

def menor():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = min(a, b)
    print(f"El menor es: {resultado}")
    guardar_historial("Menor", resultado)

def mayor():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = max(a, b)
    print(f"El mayor es: {resultado}")
    guardar_historial("Mayor", resultado)

def promedio():
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    resultado = (a + b) / 2
    print(f"El promedio es: {resultado}")
    guardar_historial("Promedio", resultado)

def factorial():
    while True:
        try:
            numero = int(input("Ingrese un numero entero no negativo: "))
            if numero < 0:
                print("Error: No se puede calcular el factorial de un numero negativo.")
            else:
                resultado = math.factorial(numero)
                print(f"Resultado: {resultado}")
                guardar_historial("Factorial", resultado)
                break
        except ValueError:
            print("Entrada invalida. Intente de nuevo.")

def numero_aleatorio():
    while True:
        try:
            minimo = int(input("Ingrese el valor minimo: "))
            maximo = int(input("Ingrese el valor maximo: "))
            if minimo > maximo:
                print("Error: El minimo no puede ser mayor que el maximo.")
            else:
                resultado = random.randint(minimo, maximo)
                print(f"Numero aleatorio generado: {resultado}")
                guardar_historial("Numero aleatorio", resultado)
                break
        except ValueError:
            print("Entrada invalida. Intente de nuevo.")

def convertir_grados():
    opcion = input("Desea convertir a (C)elsius o (F)ahrenheit?: ").strip().upper()
    temperatura = pedir_numero("Ingrese la temperatura: ")
    if opcion == "C":
        resultado = (temperatura - 32) * 5 / 9
        print(f"{temperatura}°F son {resultado:.2f}°C")
        guardar_historial("Fahrenheit a Celsius", resultado)
    elif opcion == "F":
        resultado = (temperatura * 9 / 5) + 32
        print(f"{temperatura}°C son {resultado:.2f}°F")
        guardar_historial("Celsius a Fahrenheit", resultado)
    else:
        print("Opcion invalida. Use 'C' o 'F'.")

def mostrar_menu():
    print("\n--- Calculadora Matematica ---")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Potencia")
    print("6) Raiz cuadrada")
    print("7) Modulo")
    print("8) Redondear")
    print("9) Menor")
    print("10) Mayor")
    print("11) Promedio")
    print("12) Factorial")
    print("13) Numero aleatorio")
    print("14) Conversion de grados")
    print("15) Salir")

def ejecutar_opcion(opcion):
    funciones = {
        1: sumar,
        2: restar,
        3: multiplicar,
        4: dividir,
        5: potencia,
        6: raiz_cuadrada,
        7: modulo,
        8: redondear,
        9: menor,
        10: mayor,
        11: promedio,
        12: factorial,
        13: numero_aleatorio,
        14: convertir_grados
    }
    funcion = funciones.get(opcion)
    if funcion:
        funcion()
    elif opcion == 15:
        print("Gracias por usar la calculadora.")
        exit()
    else:
        print("Opcion invalida. Intente de nuevo.")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opcion (1-15): "))
        ejecutar_opcion(opcion)
    except ValueError:
        print("Entrada invalida. Ingrese un numero del 1 al 15.")
    continuar = input("Desea realizar otra operacion? (s/n): ").strip().lower()
    if continuar != "s":
        print("Hasta luego.")
        break
