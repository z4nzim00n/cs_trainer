using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // SortedDictionary сразу сортирует значения.
        var counts = new SortedDictionary<int, int>();
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (counts.ContainsKey(value))
            {
                counts[value]++;
            }
            else
            {
                counts[value] = 1;
            }
        }

        foreach (var pair in counts)
        {
            // new string повторяет символ нужное число раз.
            string stars = new string('*', pair.Value);
            Console.WriteLine($"{pair.Key}: {stars}");
        }
    }
}
