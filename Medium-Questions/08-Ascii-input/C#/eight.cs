using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ascii
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a single character");
            string temp = Console.ReadLine();

            if (temp.Length > 1)
            {
                Console.WriteLine("Input is not a Single Character");
                Console.ReadKey();
                return;
            }


            byte[] ASCIIvalues = Encoding.ASCII.GetBytes(temp);
            foreach (var c in ASCIIvalues)
            {
                if (c >= 48 && c <= 57)
                {
                    Console.WriteLine("Number :) ");
                }
                else if (c >= 65 && c <= 97)
                {
                    Console.WriteLine("Uper case Alphabet :) ");
                }
                else if (c >= 97 && c <= 122)
                {
                    Console.WriteLine("Lower case Alphabet :) ");
                }
                else
                {
                    Console.WriteLine("its a symbol");
                }

            }

            Console.ReadKey();
        }
    }
}
