# Разбор задания

## Чтение и разбор

~~~csharp
string text = File.ReadAllText(path);
string[] parts = text.Split(
    new char[] { ' ', '\t', '\r', '\n' },
    StringSplitOptions.RemoveEmptyEntries);
~~~

`RemoveEmptyEntries` убирает пустые куски между разделителями.

## Сумма

~~~csharp
long sum = 0;
foreach (string part in parts)
{
    sum += int.Parse(part);
}
~~~

`long` защищает от переполнения при большом количестве чисел.

## Альтернатива по строкам

~~~csharp
foreach (string line in File.ReadAllLines(path))
{
    foreach (string part in line.Split(' '))
    {
        // ...
    }
}
~~~

## Файла нет

`ReadAllText` бросит `FileNotFoundException`. Обработайте её, если файл
может отсутствовать.
