# Разбор задания

## Множество

`HashSet<T>` хранит только уникальные значения:

~~~csharp
var unique = new HashSet<int>();
foreach (int x in numbers)
{
    unique.Add(x);
}
~~~

`Add` возвращает `false`, если элемент уже был. Повторное добавление
ничего не меняет.

## Количество

~~~csharp
Console.WriteLine($"Unique: {unique.Count}");
~~~

## Сортировка

Порядок в `HashSet` не определён. Для вывода соберите значения в список:

~~~csharp
var result = new List<int>(unique);
result.Sort();
Console.WriteLine(string.Join(" ", result));
~~~

## Сложность

`Add` в среднем `O(1)`, сортировка `O(k log k)`, где `k` — число
уникальных значений.
