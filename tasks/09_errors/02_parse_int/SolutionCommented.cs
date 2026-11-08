using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();

        // TryParse не бросает исключение — возвращает true или false.
        if (int.TryParse(input, out int value))
        {
            Console.WriteLine($"Number: {value}");
        }
        else
        {
            Console.WriteLine("Invalid number");
        }
    }
}
