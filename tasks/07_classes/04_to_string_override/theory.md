# Разбор задания

## `ToString` у объекта

`Console.WriteLine(object)` вызывает `ToString()`. По умолчанию возвращается
полное имя типа, например `Point`.

## Переопределение

~~~csharp
class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public override string ToString()
    {
        return $"Point({X}, {Y})";
    }
}
~~~

- `override` обязателен: метод уже объявлен в `object`.
- Сигнатура должна совпадать: `public override string ToString()`.
- `Console.WriteLine($"...{p}")` тоже использует `ToString()`.

## Зачем

Единый текстовый вид объекта удобен для отладки, логов и вывода в консоль.
