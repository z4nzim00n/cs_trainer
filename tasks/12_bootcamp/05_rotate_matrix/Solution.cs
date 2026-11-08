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

        for (int i = 0; i < n; ++i)
        {
            string[] row = new string[n];
            for (int j = 0; j < n; ++j)
            {
                row[j] = a[n - 1 - j, i].ToString();
            }
            Console.WriteLine(string.Join(" ", row));
        }
    }
}
