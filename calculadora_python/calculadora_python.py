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




