using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        int ticket = int.Parse(parts[1]);

        // Нужны одновременно возраст 18+ и билет.
        bool allowed = age >= 18 && ticket == 1;
        Console.WriteLine($"Allowed: {allowed}");
    }
}
