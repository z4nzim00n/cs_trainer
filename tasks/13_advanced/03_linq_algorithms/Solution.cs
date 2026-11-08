using System;
using System.Linq;

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

        int sum = numbers
            .Where(x => x % 2 == 0)
            .Select(x => x * x)
            .Sum();

        Console.WriteLine($"Sum: {sum}");
    }
}
