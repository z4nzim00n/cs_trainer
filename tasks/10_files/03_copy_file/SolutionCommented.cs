using System;
using System.IO;

class Program
{
    static void Main()
    {
        string source = Console.ReadLine();
        string destination = Console.ReadLine();

        // true разрешает перезаписать существующий файл.
        File.Copy(source, destination, true);
        Console.WriteLine($"Copied: {destination}");
    }
}
