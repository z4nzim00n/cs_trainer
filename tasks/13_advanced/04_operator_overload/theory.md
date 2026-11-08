# Разбор задания

## Перегрузка оператора

Оператор объявляется как статический метод с ключевым словом `operator`:

~~~csharp
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
}
~~~

## Вызов

~~~csharp
Vector c = a + b;
~~~

Компилятор превращает это в `Vector.op_Addition(a, b)`.

## Правила

- Хотя бы один параметр должен быть типом, в котором объявлен оператор.
- Нельзя изменить смысл встроенных операторов для встроенных типов.
- Операторы `==` и `!=` перегружают парой, иначе ошибка компиляции.

## Вывод

~~~csharp
Console.WriteLine($"{c.X}, {c.Y}");
~~~

Можно переопределить `ToString()` и печатать объект целиком.
