using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Invariant не зависит от локали машины.
        Console.WriteLine($"UPPER: {line.ToUpperInvariant()}");
        Console.WriteLine($"lower: {line.ToLowerInvariant()}");
    }
}
