using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        int max = int.MinValue;
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (value > max)
            {
                max = value;
            }
        }

        Console.WriteLine($"Max: {max}");
    }
}
