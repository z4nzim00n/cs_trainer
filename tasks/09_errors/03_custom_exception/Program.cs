using System;

class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}

class Program
{
    static void Main()
    {
        int age = int.Parse(Console.ReadLine());

        // TODO: брось NegativeAgeException для возраста < 0
        Console.WriteLine("TODO");
    }
}
