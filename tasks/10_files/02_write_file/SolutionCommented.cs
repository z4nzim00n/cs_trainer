using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = Console.ReadLine();

        // WriteAllText создаёт файл или перезаписывает существующий.
        File.WriteAllText(path, text);
        Console.WriteLine($"Written: {path}");
    }
}
