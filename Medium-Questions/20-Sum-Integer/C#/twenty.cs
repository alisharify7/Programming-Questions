using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.Write("Enter a Number: ");
            string input = Console.ReadLine();
            int number;
            try
            {
                number = int.Parse(input);
            }
            catch
            {
                Console.WriteLine("NaN");
                return;
            }

            Console.WriteLine((number * (number + 1) / 2));

            Console.ReadKey();
        }
    }
}
