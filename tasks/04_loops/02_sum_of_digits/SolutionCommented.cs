using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // На каждой итерации отделяем последнюю цифру и убираем её.
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
