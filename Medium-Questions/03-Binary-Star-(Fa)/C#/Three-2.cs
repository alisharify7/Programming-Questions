using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ThreeOO
{
    class Program
    {

        // this function take a number and 
        // print star
        static void print_star(int number)
        {
            // safety check
            if (number < 0)
            {
                Console.Write("Error");
            }

            // This for loop is for Row
            for (int i = 1; i <= number; i++)
            {
                // this for loop is for print Star
                for (int j = 0; j < i; j++)
                {
                    Console.Write("*");
                }
                // Print New Line 
                Console.WriteLine("");
            }

        }


        static void Main(string[] args)
        {

            // Test the Function
            print_star(15);


            Console.ReadKey();
        }

    }
}
