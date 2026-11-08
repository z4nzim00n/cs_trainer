using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var words = new List<string>();
        for (int i = 0; i < n; ++i)
        {
            words.Add(parts[i]);
        }

        // Составное сравнение: длина, при равенстве — коды символов.
        words.Sort((x, y) =>
        {
            int cmp = x.Length.CompareTo(y.Length);
            return cmp != 0 ? cmp : string.CompareOrdinal(x, y);
        });

        Console.WriteLine(string.Join(" ", words));
    }
}
