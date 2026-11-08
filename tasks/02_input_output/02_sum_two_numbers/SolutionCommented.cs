using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // Сначала вычисляем, потом печатаем.
        int sum = a + b;
        Console.WriteLine($"Sum: {sum}");
    }
}
