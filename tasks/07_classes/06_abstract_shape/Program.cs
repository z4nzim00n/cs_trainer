using System;
using System.Globalization;

abstract class Shape
{
    public abstract double Area();
}

class Circle : Shape
{
    public double R;

    public Circle(double r)
    {
        R = r;
    }

    public override double Area()
    {
        // TODO: верни площадь круга
        return 0;
    }
}

class Rectangle : Shape
{
    public double W;
    public double H;

    public Rectangle(double w, double h)
    {
        W = w;
        H = h;
    }

    public override double Area()
    {
        // TODO: верни площадь прямоугольника
        return 0;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: создай нужную фигуру и выведи Area: X.XX
        Console.WriteLine("TODO");
    }
}
