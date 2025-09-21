﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace proyecto3384
{
    class Program
    {
        static void Main(string[] args)
        {
            bool continuar = true;

            while (continuar)
            {
                MostrarMenu();
                Console.Write("¿Desea realizar otra operación? (s/n): ");
                string respuesta = Console.ReadLine().ToLower();
                if (respuesta != "s")
                {
                    continuar = false;
                    Console.WriteLine("Programa finalizado.");
                }
            }
        }


        static void MostrarMenu()
        {
            Console.WriteLine("Bienvenido al sistema de operaciones básicas");
            Console.WriteLine("Seleccione una opción del menú:"); 
            Console.WriteLine("1. Sumar");
            Console.WriteLine("2. Restar");
            Console.WriteLine("3. Multiplicar");
            Console.WriteLine("4. Dividir");
            Console.WriteLine("5. Salir");
            Console.Write("Seleccione una opción: ");
            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1": Sumar(); break;
                case "2": Restar(); break;
                    
                case "3": Multiplicar(); break;

                case "4": Dividir(); break;

                case "5": Salir(); break;

                default: Console.WriteLine("Opción inválida"); break;
            }
        }

        static void Sumar()
        {
            Console.Write("Ingrese el primer número: ");
            if (!int.TryParse(Console.ReadLine(), out int a))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.Write("Ingrese el segundo número: ");
            if (!int.TryParse(Console.ReadLine(), out int b))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.WriteLine($"Resultado: {a + b}");
        }



        static void Restar()
        {
            Console.Write("Ingrese el primer número: ");
            if (!int.TryParse(Console.ReadLine(), out int a))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.Write("Ingrese el segundo número: ");
            if (!int.TryParse(Console.ReadLine(), out int b))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.WriteLine($"Resultado: {a - b}");
        }


        static void Multiplicar()
        {
            Console.Write("Ingrese el primer número: ");
            if (!int.TryParse(Console.ReadLine(), out int a))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.Write("Ingrese el segundo número: ");
            if (!int.TryParse(Console.ReadLine(), out int b))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.WriteLine($"Resultado: {a * b}");
        }


        static void Dividir()
        {
            Console.Write("Ingrese el numerador: ");
            if (!int.TryParse(Console.ReadLine(), out int a))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            Console.Write("Ingrese el denominador: ");
            if (!int.TryParse(Console.ReadLine(), out int b))
            {
                Console.WriteLine("Entrada inválida. Debe ingresar un número.");
                return;
            }

            if (b == 0)
            {
                Console.WriteLine("No se puede dividir entre cero.");
            }
            else
            {
                Console.WriteLine($"Resultado: {a / b}");
            }
        }



        static void Salir()
        {
            Console.Write("¿Está seguro que desea salir? (s/n): ");
            string respuesta = Console.ReadLine().ToLower();

            if (respuesta == "s")
            {
                Console.WriteLine("Gracias por usar el programa.");
            }
            else
            {
                MostrarMenu();
            }
        }

    }
}
