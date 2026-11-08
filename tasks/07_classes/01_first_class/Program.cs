using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        // TODO: создай Point и выведи его координаты
        Console.WriteLine("TODO");
    }
}
