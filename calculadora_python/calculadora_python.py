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




