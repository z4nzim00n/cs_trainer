using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radians = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // 180 / π — коэффициент перевода радиан в градусы.
        double degrees = radians * 180.0 / Math.PI;
        Console.WriteLine("Degrees: " + degrees.ToString("F2", CultureInfo.InvariantCulture));
    }
}
