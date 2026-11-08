using System;

class Program
{
    static void Main()
    {
        string[] header = Console.ReadLine().Split(' ');
        int n = int.Parse(header[0]);
        int k = int.Parse(header[1]);
        string[] parts = Console.ReadLine().Split(' ');

        k = k % n;
        int[] result = new int[n];
        for (int i = 0; i < n; ++i)
        {
            result[(i + k) % n] = int.Parse(parts[i]);
        }

        Console.WriteLine(string.Join(" ", result));
    }
}
