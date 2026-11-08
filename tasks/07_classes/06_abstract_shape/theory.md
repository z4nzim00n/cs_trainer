# Разбор задания

## Абстрактный класс

~~~csharp
abstract class Shape
{
    public abstract double Area();
}
~~~

У метода нет тела: каждый наследник обязан его реализовать. Создать
`new Shape()` нельзя — это ошибка компиляции.

## Наследники

~~~csharp
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
~~~

## Полиморфный вызов

~~~csharp
Shape shape = new Circle(r);
double area = shape.Area();
~~~

`Shape` задаёт контракт, наследники — конкретную формулу.

## Формат числа

~~~csharp
using System.Globalization;
...
area.ToString("F2", CultureInfo.InvariantCulture)
~~~

`F2` — два знака после точки. `InvariantCulture` гарантирует точку,
а не запятую.

## Разбор ввода

~~~csharp
string[] parts = line.Split(' ');
if (parts[0] == "circle") { ... }
else { ... }
~~~
