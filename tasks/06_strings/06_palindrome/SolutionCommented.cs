using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        string reversed = new string(chars);

        // == у string сравнивает содержимое.
        Console.WriteLine(line == reversed);
    }
}
