using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = Console.ReadLine();

        File.WriteAllText(path, text);
        Console.WriteLine($"Written: {path}");
    }
}
