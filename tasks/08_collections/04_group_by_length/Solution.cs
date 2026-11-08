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

        var groups = new SortedDictionary<int, List<string>>();
        foreach (string word in words)
        {
            if (!groups.ContainsKey(word.Length))
            {
                groups[word.Length] = new List<string>();
            }
            groups[word.Length].Add(word);
        }

        foreach (var pair in groups)
        {
            pair.Value.Sort();
            Console.WriteLine($"{pair.Key}: {string.Join(" ", pair.Value)}");
        }
    }
}
