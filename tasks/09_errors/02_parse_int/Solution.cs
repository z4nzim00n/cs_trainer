using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();
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
