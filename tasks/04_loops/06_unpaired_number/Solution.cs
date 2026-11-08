using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        int result = 0;
        for (int i = 0; i < n; ++i)
        {
            result ^= int.Parse(parts[i]);
        }

        Console.WriteLine($"Unique: {result}");
    }
}
