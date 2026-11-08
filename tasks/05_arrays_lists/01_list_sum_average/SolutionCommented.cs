using System;
using System.Collections.Generic;
using System.Globalization;

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

        long sum = 0;
        foreach (int x in numbers)
        {
            sum += x;
        }

        // Приводим sum к double, иначе деление будет целочисленным.
        double average = (double)sum / n;
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
