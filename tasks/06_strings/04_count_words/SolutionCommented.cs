using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // RemoveEmptyEntries убирает куски между соседними пробелами.
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
