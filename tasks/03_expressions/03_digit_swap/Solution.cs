using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        int thousands = n / 1000;
        int middle = n / 10 % 100;
        int units = n % 10;

        int result = units * 1000 + middle * 10 + thousands;
        Console.WriteLine(result);
    }
}
