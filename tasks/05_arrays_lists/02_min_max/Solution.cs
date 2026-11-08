using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        int min = int.MaxValue;
        int max = int.MinValue;
        foreach (int x in numbers)
        {
            if (x < min) min = x;
            if (x > max) max = x;
        }

        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
    }
}
