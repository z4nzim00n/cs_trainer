using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        int letters = 0;
        int digits = 0;
        // foreach по string даёт char — один символ UTF-16.
        foreach (char c in line)
        {
            if (char.IsLetter(c)) letters++;
            if (char.IsDigit(c)) digits++;
        }

        Console.WriteLine($"Letters: {letters}");
        Console.WriteLine($"Digits: {digits}");
    }
}
