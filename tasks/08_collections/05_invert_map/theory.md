# Разбор задания

## Что значит инверсия

Было `ключ → число`, стало `число → ключ`:

~~~csharp
int n = int.Parse(Console.ReadLine());
var inverted = new SortedDictionary<int, string>();
for (int i = 0; i < n; ++i)
{
    string[] parts = Console.ReadLine().Split(' ');
    string key = parts[0];
    int value = int.Parse(parts[1]);
    inverted[value] = key;
}
~~~

## Сортировка по новому ключу

`SortedDictionary<int, string>` сортирует по `int`-ключу, то есть по
исходному значению. Вывод сразу получается в нужном порядке.

## Дубликаты

Если два исходных ключа имеют одинаковое значение, второй затрёт первый:
`inverted[value] = key` заменяет запись. В задаче значения уникальны.

## Вывод

~~~csharp
foreach (var pair in inverted)
{
    Console.WriteLine($"{pair.Key}: {pair.Value}");
}
~~~
