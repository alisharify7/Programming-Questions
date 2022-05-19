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

            // get input from user
            Console.WriteLine("Enter a Number: ");
            string user = Console.ReadLine();

            // Convert input to int
            int int_user= Int32.Parse(user);
            // check to input between 1 to 100
            if (int_user < 100 && int_user > 0)
            {
                // check for Even or odd Number
                if (int_user % 2 == 0)
                {
                    Console.WriteLine("Its Even");
                }
                else
                {
                    Console.WriteLine("Its Odd");
                }

            }
            else
            {
                // if Number is not between 1 to 100
                Console.WriteLine("Its Not betweeb 1 to 100");
            }
            Console.ReadKey();
        }
    }
}
