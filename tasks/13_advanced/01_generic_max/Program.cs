using System;

class Program
{
    static T Max<T>(T a, T b) where T : IComparable<T>
    {
        // TODO: верни больший из двух
        return a;
    }

    static void Main()
    {
        string[] numbers = Console.ReadLine().Split(' ');
        string[] words = Console.ReadLine().Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);

        // TODO: выведи Max int и Max string
        Console.WriteLine("TODO");
    }
}
