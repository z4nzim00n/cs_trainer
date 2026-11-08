using System;

class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
    }

    public void Dispose()
    {
        // TODO: напечатай Close: имя
    }
}

class Program
{
    static void Main()
    {
        string name = Console.ReadLine();

        // TODO: открой ресурс через using, напечатай Use: имя
        Console.WriteLine("TODO");
    }
}
