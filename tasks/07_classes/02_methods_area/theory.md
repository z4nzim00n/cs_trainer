# Разбор задания

## Метод экземпляра

Метод объявляется внутри класса и имеет доступ к его полям:

~~~csharp
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
~~~

## Вызов

~~~csharp
Rectangle r = new Rectangle(w, h);
Console.WriteLine($"Area: {r.Area()}");
~~~

Скобки обязательны: `r.Area` без `()` — это группа методов, а не число.

## `static` или экземпляр

`static`-метод не имеет доступа к полям объекта и вызывается через имя
класса. `Area()` зависит от конкретного прямоугольника, поэтому метод
экземпляра.

## Переполнение

`int` хватает для небольших сторон. Для больших значений используйте
`long`, иначе произведение переполнится молча.
