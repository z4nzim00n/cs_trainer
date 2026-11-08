using System;
using System.IO;

class Program
{
    static void Main()
    {
        string source = Console.ReadLine();
        string destination = Console.ReadLine();

        File.Copy(source, destination, true);
        Console.WriteLine($"Copied: {destination}");
    }
}
