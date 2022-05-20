using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Two
{
    class Program
    {
        static void Main(string[] args)
        {
            // get input from user
            Console.Write("Enter a Number: ");
            string user = Console.ReadLine();
            
            // convert int to string
            int res = Int32.Parse(user);

            // this for loop is for row
            for (int i = 1; i <= res; i++)
            {
                // this for loop is for print Star
                for (int j = 0; j < i; j++)
                {
                    Console.Write("*");
                }
                // print New Line
                Console.WriteLine("");
            }

            Console.ReadKey();
        }

    }
}
