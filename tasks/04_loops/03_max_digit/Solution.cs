using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

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
