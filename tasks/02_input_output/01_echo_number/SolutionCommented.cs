using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Parse превращает текст в число.
        int number = int.Parse(line);

        Console.WriteLine($"Number: {number}");
    }
}
