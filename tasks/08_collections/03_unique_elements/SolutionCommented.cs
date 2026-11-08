using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // HashSet сам отбрасывает повторы.
        var unique = new HashSet<int>();
        for (int i = 0; i < n; ++i)
        {
            unique.Add(int.Parse(parts[i]));
        }

        // Порядок HashSet не определён — сортируем копию.
        var result = new List<int>(unique);
        result.Sort();

        Console.WriteLine($"Unique: {unique.Count}");
        Console.WriteLine(string.Join(" ", result));
    }
}
