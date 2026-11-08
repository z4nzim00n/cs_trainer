using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // Цифры лежат в 0…9, поэтому 0 — безопасное начальное значение.
        int max = 0;
        while (n > 0)
        {
            int digit = n % 10;
            if (digit > max)
            {
                max = digit;
            }
            n /= 10;
        }

        Console.WriteLine($"Max digit: {max}");
    }
}
