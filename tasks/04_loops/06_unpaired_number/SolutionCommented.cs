using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // Пары одинаковых чисел дают 0, поэтому остаётся только непарное.
        int result = 0;
        for (int i = 0; i < n; ++i)
        {
            result ^= int.Parse(parts[i]);
        }

        Console.WriteLine($"Unique: {result}");
    }
}
