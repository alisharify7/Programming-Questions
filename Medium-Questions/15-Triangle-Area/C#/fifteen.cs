using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace fifteen
{
    class Program
    {
        static void Main(string[] args)
        {

            // get input and convert it
            Console.Write("Enter width: ");
            string temp = Console.ReadLine();
            int width = Int32.Parse(temp);

            // get input and convert it
            Console.Write("Enter heigth: ");
            string temp1 = Console.ReadLine();
            int heigth = Int32.Parse(temp);

            // do calculation
            double answer = (width * heigth) * 0.5;
            Console.WriteLine("Area is {0}",answer);


            Console.ReadKey();
        }
    }
}
