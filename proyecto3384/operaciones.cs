using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace proyecto3384
{
    internal class operaciones
    {
        public static int Sumar(int a, int b) => a + b;
        public static int Restar(int a, int b) => a - b;
        public static int Multiplicar(int a, int b) => a * b;
        public static int Dividir(int a, int b)
        {
            if (b == 0) throw new DivideByZeroException();
            return a / b;
        }

    }
}
