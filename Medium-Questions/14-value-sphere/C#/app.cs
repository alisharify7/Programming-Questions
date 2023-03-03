using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace app
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //4 / 3 * p * r ** 3
            //R = 6.0
            int r = 5;
            Console.WriteLine(Math.PI);
            double result = System.Math.Pow((4 / 3) * System.Math.PI * r , 3);
            Console.WriteLine(result);
            Console.ReadKey();
                
         }

    }
}
