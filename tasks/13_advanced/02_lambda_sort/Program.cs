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

        // TODO: отсортируй по длине, затем по алфавиту
        Console.WriteLine("TODO");
    }
}
