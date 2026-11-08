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

        // TODO: поверни матрицу и выведи строки
        Console.WriteLine("TODO");
    }
}
