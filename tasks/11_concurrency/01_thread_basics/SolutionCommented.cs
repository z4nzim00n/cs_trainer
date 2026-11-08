using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Thread t = new Thread(() =>
        {
            Console.WriteLine("Hello from thread");
        });
        t.Start();
        // Join гарантирует, что поток закончит до следующей строки.
        t.Join();
        Console.WriteLine("Main done");
    }
}
