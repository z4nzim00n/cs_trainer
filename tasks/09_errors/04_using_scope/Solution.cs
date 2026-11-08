using System;

class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
        Console.WriteLine($"Open: {name}");
    }

    public void Dispose()
    {
        Console.WriteLine($"Close: {name}");
    }
}

class Program
{
    static void Main()
    {
        string name = Console.ReadLine();

        using (Resource r = new Resource(name))
        {
            Console.WriteLine($"Use: {name}");
        }
    }
}
