using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace app
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter Dates in format of YYYY/MM/DD");
            Console.Write("ENter Date One: ");
            string date_one = Console.ReadLine();

            Console.Write("ENter Date Two: ");
            string date_two = Console.ReadLine();
            
            string[] date_one_arr = (date_one.Split('/'));
            string[] date_two_arr = (date_two.Split('/'));

            if (date_one_arr.Length != 3 || date_two_arr.Length != 3)
            {
                Console.WriteLine("Invalid Date;");
                return;
            }
            try
            {
                DateTime dt1 = new DateTime(year: Convert.ToInt32(date_one_arr[0]), month: Convert.ToInt32(date_one_arr[1]), day: Convert.ToInt32(date_one_arr[2])) ;
                DateTime dt2 = new DateTime(year: Convert.ToInt32(date_two_arr[0]), month: Convert.ToInt32(date_two_arr[1]), day: Convert.ToInt32(date_two_arr[2])) ;
                Console.WriteLine(string.Format("{0:d} Days ", Convert.ToString((dt1 - dt2).Days)) );
            }
            catch (Exception)
            {

                throw;
            }
            Console.ReadKey(); 
                
         }

    }
}
