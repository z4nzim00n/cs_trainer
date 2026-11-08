using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int index = int.Parse(Console.ReadLine());

        // TODO: выведи numbers[index] или сообщение об ошибке
        Console.WriteLine("TODO");
    }
}
