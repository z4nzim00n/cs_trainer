using System;

class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    public static Vector operator +(Vector a, Vector b)
    {
        return new Vector(a.X + b.X, a.Y + b.Y);
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Vector a = new Vector(int.Parse(parts[0]), int.Parse(parts[1]));
        Vector b = new Vector(int.Parse(parts[2]), int.Parse(parts[3]));

        Vector c = a + b;
        Console.WriteLine(c);
    }
}
