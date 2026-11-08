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

    // TODO: перегрузи оператор +
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Vector a = new Vector(int.Parse(parts[0]), int.Parse(parts[1]));
        Vector b = new Vector(int.Parse(parts[2]), int.Parse(parts[3]));

        // TODO: сложи векторы и выведи результат
        Console.WriteLine("TODO");
    }
}
