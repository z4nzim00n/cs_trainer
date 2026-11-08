using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        // F2 — два знака после точки; InvariantCulture фиксирует точку.
        string text = value.ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine("Value: " + text);
    }
}
