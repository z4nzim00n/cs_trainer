using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        Console.WriteLine(new string(chars));
    }
}
