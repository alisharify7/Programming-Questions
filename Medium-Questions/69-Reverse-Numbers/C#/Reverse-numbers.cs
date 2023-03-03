using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reverse_Numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int height = 8;
            int counter = height;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < counter; j++)
                {
                    Console.Write(i+1 + " ");
                }
                counter--;
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
