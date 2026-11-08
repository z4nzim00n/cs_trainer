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
        // TODO: верни площадь
        return 0;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int w = int.Parse(parts[0]);
        int h = int.Parse(parts[1]);

        // TODO: создай Rectangle и выведи Area
        Console.WriteLine("TODO");
    }
}
