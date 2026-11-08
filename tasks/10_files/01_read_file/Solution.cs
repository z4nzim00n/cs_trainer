using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        try
        {
            string text = File.ReadAllText(path);
            Console.Write(text);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Error: file not found");
        }
    }
}
