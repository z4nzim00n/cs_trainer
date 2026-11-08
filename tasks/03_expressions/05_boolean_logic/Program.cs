using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        int ticket = int.Parse(parts[1]);

        // TODO: вычисли, проходит ли человек, и выведи Allowed: True/False
        bool allowed = false;
        Console.WriteLine($"Allowed: {allowed}");
    }
}
