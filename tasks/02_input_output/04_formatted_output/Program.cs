using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        // TODO: выведи Value: <значение с двумя знаками>
        Console.WriteLine("TODO");
    }
}
