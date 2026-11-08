using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // Временная переменная сохраняет a, пока мы записываем в неё b.
        int temp = a;
        a = b;
        b = temp;

        Console.WriteLine(a + " " + b);
    }
}
