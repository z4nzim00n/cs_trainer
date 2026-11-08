using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        string text = value.ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine("Value: " + text);
    }
}
