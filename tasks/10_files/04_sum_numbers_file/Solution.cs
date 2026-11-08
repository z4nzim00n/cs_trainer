using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);
        string[] parts = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);

        long sum = 0;
        foreach (string part in parts)
        {
            sum += int.Parse(part);
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
