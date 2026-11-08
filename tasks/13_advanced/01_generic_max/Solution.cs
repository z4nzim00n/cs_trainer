using System;

class Program
{
    static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) >= 0 ? a : b;
    }

    static void Main()
    {
        string[] numbers = Console.ReadLine().Split(' ');
        string[] words = Console.ReadLine().Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);

        Console.WriteLine($"Max int: {Max(a, b)}");
        Console.WriteLine($"Max string: {Max(words[0], words[1])}");
    }
}
