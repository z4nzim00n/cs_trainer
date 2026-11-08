using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        int m = int.Parse(parts[1]);

        int counter = 0;
        // Один объект-замок на все потоки.
        object gate = new object();
        Thread[] threads = new Thread[n];
        for (int i = 0; i < n; ++i)
        {
            threads[i] = new Thread(() =>
            {
                for (int j = 0; j < m; ++j)
                {
                    lock (gate)
                    {
                        counter++;
                    }
                }
            });
            threads[i].Start();
        }
        foreach (Thread t in threads)
        {
            t.Join();
        }

        Console.WriteLine($"Counter: {counter}");
    }
}
