using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // У каждого потока своя ячейка — общих записей нет.
        int[] results = new int[2];
        Thread t1 = new Thread(() => results[0] = a * a);
        Thread t2 = new Thread(() => results[1] = b * b);
        t1.Start();
        t2.Start();
        t1.Join();
        t2.Join();

        Console.WriteLine($"A: {results[0]}");
        Console.WriteLine($"B: {results[1]}");
    }
}
