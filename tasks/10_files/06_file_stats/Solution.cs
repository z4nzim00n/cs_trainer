using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string[] lines = File.ReadAllLines(path);

        int words = 0;
        int chars = 0;
        foreach (string line in lines)
        {
            words += line.Split(
                new char[] { ' ', '\t' },
                StringSplitOptions.RemoveEmptyEntries).Length;
            foreach (char c in line)
            {
                if (!char.IsWhiteSpace(c))
                {
                    chars++;
                }
            }
        }

        Console.WriteLine($"Lines: {lines.Length}");
        Console.WriteLine($"Words: {words}");
        Console.WriteLine($"Chars: {chars}");
    }
}
