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

        try
        {
            if (age < 0)
            {
                throw new NegativeAgeException("age cannot be negative");
            }
            Console.WriteLine($"Age: {age}");
        }
        catch (NegativeAgeException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
