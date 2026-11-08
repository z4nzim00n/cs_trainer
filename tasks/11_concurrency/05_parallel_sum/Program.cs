using System;
using System.Threading.Tasks;

class Program
{
    static long Sum(int[] numbers, int from, int to)
    {
        // TODO: сложи элементы диапазона
        return 0;
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

        // TODO: сложи две половины в задачах
        Console.WriteLine("TODO");
    }
}
