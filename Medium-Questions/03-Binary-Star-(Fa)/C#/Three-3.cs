using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace threeO
{
    class Program
    {
        // this function take a number and Print Star With it
        static void print_star(int number)
        {
            // safety check
            if (number < 0)
            {
                Console.Write("Error");
            }

            // This for loop is for Row
            for (int i = 1; i <= number; i++)
            {
                // this for loop is for print Star
                for (int j = 0; j < i; j++)
                {
                    Console.Write("*");
                }
                // Print New Line 
                Console.WriteLine("");
            }

        }


        // This function take A number and return number of 1 in Binary
        static int bin_num(int number)
        {

            int counter = 0;

            // convert int number to Binary number 
            string binary = Convert.ToString(number, 2);

            // iterate over all string
            foreach (char one in binary)
            {
                // if i element is string equal to 1
                if (one == '1')
                {
                    counter++;
                }
            }

            // return Number of One in binaary
            return counter;

        }

        static void Main(string[] args)
        {
            // get input from user
            Console.Write("Enter a Number: ");
            string user = Console.ReadLine();
            // convert string to int
            int temp = Int32.Parse(user);

            // get number of 1 in user input
            int bin_number = bin_num(temp);

            // print star
            print_star(bin_number);


            Console.ReadKey();

        }
    }
}
