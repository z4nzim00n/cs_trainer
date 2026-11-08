using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int min = int.MaxValue;
        int max = int.MinValue;
        long sum = 0;
        for (int i = 0; i < n; ++i)
        {
            int x = numbers[i];
            if (x < min) min = x;
            if (x > max) max = x;
            sum += x;
        }

        // (double) обязателен для дробного среднего.
        double average = (double)sum / n;
        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
