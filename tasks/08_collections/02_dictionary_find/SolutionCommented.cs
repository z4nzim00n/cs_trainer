using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var map = new Dictionary<string, int>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            map[parts[0]] = int.Parse(parts[1]);
        }

        string query = Console.ReadLine();

        // TryGetValue безопасно сообщает, есть ли ключ.
        if (map.TryGetValue(query, out int value))
        {
            Console.WriteLine($"Found: {value}");
        }
        else
        {
            Console.WriteLine("Not found");
        }
    }
}
