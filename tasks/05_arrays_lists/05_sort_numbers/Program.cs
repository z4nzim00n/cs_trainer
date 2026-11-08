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

        // TODO: отсортируй список и выведи числа через пробел
        Console.WriteLine("TODO");
    }
}
