using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine());

        long reversed = 0;
        while (n > 0)
        {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        Console.WriteLine(reversed);
    }
}
