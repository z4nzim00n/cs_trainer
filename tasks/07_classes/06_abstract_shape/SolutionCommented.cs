using System;
using System.Globalization;

abstract class Shape
{
    // Абстрактный метод без тела: контракт для наследников.
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
        return Math.PI * R * R;
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
        return W * H;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Shape shape;
        if (parts[0] == "circle")
        {
            double r = double.Parse(parts[1], CultureInfo.InvariantCulture);
            shape = new Circle(r);
        }
        else
        {
            double w = double.Parse(parts[1], CultureInfo.InvariantCulture);
            double h = double.Parse(parts[2], CultureInfo.InvariantCulture);
            shape = new Rectangle(w, h);
        }

        // F2 и InvariantCulture дают точку и ровно два знака.
        string area = shape.Area().ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine($"Area: {area}");
    }
}
