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

        try
        {
            int value = numbers[index];
            Console.WriteLine($"Value: {value}");
        }
        catch (IndexOutOfRangeException)
        {
            Console.WriteLine("Error: index out of range");
        }
    }
}
