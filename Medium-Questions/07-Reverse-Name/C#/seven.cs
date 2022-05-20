using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace seven
{
    class Program
    {

        public static string Reverse(string s)
        {
            // convert to array
            char[] charArray = s.ToCharArray();
            // Reverse Array
            Array.Reverse(charArray);
            // return result
            return new string(charArray);
        }

        static void Main(string[] args)
        {
            Console.Write("Enter Your Name: ");
            string name = Console.ReadLine();
            name = Reverse(name);

            Console.Write(name);

            Console.ReadKey();
        }
    }
}
