using System;

class Rectangle
{
    public int Width;
    public int Height;

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int Area()
    {
        return Width * Height;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int w = int.Parse(parts[0]);
        int h = int.Parse(parts[1]);

        Rectangle r = new Rectangle(w, h);
        Console.WriteLine($"Area: {r.Area()}");
    }
}
