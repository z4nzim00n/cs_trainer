using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radius = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // Math.PI — встроенная константа; F2 оставляет два знака.
        double area = Math.PI * radius * radius;
        Console.WriteLine("Area: " + area.ToString("F2", CultureInfo.InvariantCulture));
    }
}
