using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        Console.WriteLine($"UPPER: {line.ToUpperInvariant()}");
        Console.WriteLine($"lower: {line.ToLowerInvariant()}");
    }
}
