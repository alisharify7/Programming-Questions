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
            // way One -
            int height = 8;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < height-i; j++)
                {
                    Console.Write(i+1 + " ");
                }
                Console.WriteLine();
            }
            Console.ReadKey();

            // way two -
//             int height = 8;
//             int counter = height;
//             for (int i = 0; i < height; i++)
//             {
//                 for (int j = 0; j < counter; j++)
//                 {
//                     Console.Write(i+1 + " ");
//                 }
//                 counter--;
//                 Console.WriteLine();
//             }
//             Console.ReadKey();

        
        }
    }
}

