using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Five
{
    class Program
    {

        // this Function Return True if number is True 
        // otherwise Return False

        static bool Even_odd(int number)
        {
            if (number % 2 == 0)
            {
                return true;
            }
            return false;


        }

        static void Main(string[] args)
        {
            // Get input From user
            Console.Write("Enter a Number: ");
            string user = Console.ReadLine();

            // convert string to int
            int user_in = Int32.Parse(user);


            while (true)
            {
                // If n is 1 break
                if (user_in == 1)
                {
                    Console.WriteLine("user is {0} ", user_in);
                    break;
                   
                }
                // if user input is Even divided by 2
                if (Even_odd(user_in) == true)
                {
                    Console.WriteLine("user is {0}", user_in);
                    user_in = user_in / 2;
                    continue;
                }
                // if user input is odd
                // multiplies  it by 3
                if (Even_odd(user_in) == false)
                {
                    Console.WriteLine("user is {0}", user_in);
                    user_in = user_in * 3;
                    user_in++;
                    continue;
                }

            }

            Console.ReadKey();
        }
    }
}
