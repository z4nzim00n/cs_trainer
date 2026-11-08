# Разбор задания

## Чтение числа

~~~csharp
string line = Console.ReadLine();
int number = int.Parse(line);
~~~

`ReadLine` возвращает строку. `int.Parse` разбирает её как целое число.

## Вывод

~~~csharp
Console.WriteLine($"Number: {number}");
~~~

Интерполяция `$"..."` подставляет значение в фигурные скобки.

## Что если ввести не число

`int.Parse("abc")` бросает `FormatException`. Позже, в разделе про
исключения, мы научимся обрабатывать такие случаи через `int.TryParse`.
