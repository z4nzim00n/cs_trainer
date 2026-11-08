using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        var counts = new Dictionary<string, int>();
        foreach (string word in words)
        {
            if (counts.TryGetValue(word, out int count))
            {
                counts[word] = count + 1;
            }
            else
            {
                counts[word] = 1;
            }
        }

        var keys = new List<string>(counts.Keys);
        keys.Sort();
        foreach (string key in keys)
        {
            Console.WriteLine($"{key}: {counts[key]}");
        }
    }
}
