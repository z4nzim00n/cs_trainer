using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);
        string[] words = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
