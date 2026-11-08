using System;
using System.Threading.Tasks;

class Program
{
    static long Sum(int[] numbers, int from, int to)
    {
        // Диапазон [from, to) — половина массива.
        long sum = 0;
        for (int i = from; i < to; ++i)
        {
            sum += numbers[i];
        }
        return sum;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int mid = n / 2;
        Task<long> left = Task.Run(() => Sum(numbers, 0, mid));
        Task<long> right = Task.Run(() => Sum(numbers, mid, n));
        Task.WaitAll(left, right);

        Console.WriteLine($"Sum: {left.Result + right.Result}");
    }
}
