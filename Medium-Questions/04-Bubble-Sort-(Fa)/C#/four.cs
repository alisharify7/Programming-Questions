using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bubble
{
    class Program
    {

        //this function print a array
        static void out_arr(int[] array_input)
        {

            for (int i =0; i < (array_input.Length - 1); i++)
            {
                Console.Write(array_input[i] + " ");
            }
            Console.WriteLine(" \n - - - \n ");

        }


        static void Main(string[] args)
        {
            int[] array = {10,9,8,7,6,5,4,3,2,1};

            //10 * 10 option
            for (int i = 0; i < (array.Length - 1); i++)
            {
                for (int j = 0; j < (array.Length - 1); j++)
                {
                    //print each time array
                    out_arr(array);

                if (j + 1 > (array.Length - 1))
                {
                    continue;
                }

                int temp = array[j];
                if (temp > array[j + 1])
                {
                    //swap values
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }

              }
            }
            Console.ReadKey();
        }
    }
}
