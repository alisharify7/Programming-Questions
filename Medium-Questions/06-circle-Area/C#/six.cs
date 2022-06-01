using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace six
{
    class Program
    {
        static void Main(string[] args)
        {

            // get input from user
            Console.Write("Enter R: ");
            string temp = Console.ReadLine();
            int r = Int32.Parse(temp);

            // calculate result 
            // c = 2pr
            double answer = (3.1415 * (r ** 2) );
            Console.WriteLine("Answer is {0}", answer);

            Console.ReadKey();
        }
    }
}
