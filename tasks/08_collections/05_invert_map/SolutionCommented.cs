using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // Ключом становится число — SortedDictionary упорядочит по нему.
        var inverted = new SortedDictionary<int, string>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            inverted[int.Parse(parts[1])] = parts[0];
        }

        foreach (var pair in inverted)
        {
            Console.WriteLine($"{pair.Key}: {pair.Value}");
        }
    }
}
