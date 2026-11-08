using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine());

        // long нужен, потому что развёрнутое число может не влезть в int.
        long reversed = 0;
        while (n > 0)
        {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        Console.WriteLine(reversed);
    }
}
