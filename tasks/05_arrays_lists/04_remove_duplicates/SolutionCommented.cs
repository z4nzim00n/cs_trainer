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

        // Add возвращает false, если число уже встречалось.
        var seen = new HashSet<int>();
        var result = new List<int>();
        foreach (int x in numbers)
        {
            if (seen.Add(x))
            {
                result.Add(x);
            }
        }

        Console.WriteLine(string.Join(" ", result));
    }
}
