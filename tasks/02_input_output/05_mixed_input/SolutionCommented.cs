using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');

        // parts[0] — текст числа, parts[1] — имя.
        int age = int.Parse(parts[0]);
        string name = parts[1];

        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"Name: {name}");
    }
}
