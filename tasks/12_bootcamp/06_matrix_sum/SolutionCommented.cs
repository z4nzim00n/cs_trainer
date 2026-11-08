using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        long sum = 0;
        long diagonal = 0;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                sum += a[i, j];
                // Элементы главной диагонали лежат там, где i == j.
                if (i == j)
                {
                    diagonal += a[i, j];
                }
            }
        }

        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Diagonal: {diagonal}");
    }
}
