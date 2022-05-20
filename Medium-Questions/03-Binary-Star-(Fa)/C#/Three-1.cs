using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ThreeOOO
{
    class Program
    {

        // deifnd a function that take a Number
        // and return number on One In that Number in binary\
         
        static int bin_num(int number) {

            int counter = 0;
 
            // convert int number to Binary number 
            string binary = Convert.ToString(number, 2);

            // iterate over all string
            foreach (char one in binary)
            {
                // if i element is string equal to 1
                if(one == '1')
                {
                    counter++;
                }
            }

            // return Number of One in binaary
            return counter;

        }

        static void Main(string[] args)
        {
            // Get input From User
            Console.Write("Enter a Number: ");
            string user = Console.ReadLine();
            // Convert string Input to Int
            int user_in = Int32.Parse(user);
            
            // Send Int value To bin_num Function to 
            // Return Number of 1 in it
            int answer = bin_num(user_in);

            // print result
            Console.WriteLine(answer);


            Console.ReadKey();
        }
    }
}
