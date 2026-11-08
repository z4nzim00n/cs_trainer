# Разбор задания

## `Comparison<T>`

`List<T>.Sort` принимает делегат сравнения:

~~~csharp
words.Sort((x, y) => x.Length.CompareTo(y.Length));
~~~

Лямбда возвращает:

- отрицательное число, если `x` должен идти раньше;
- ноль, если порядок не важен;
- положительное число, если `x` должен идти позже.

## Составной порядок

~~~csharp
words.Sort((x, y) =>
{
    int cmp = x.Length.CompareTo(y.Length);
    return cmp != 0 ? cmp : string.CompareOrdinal(x, y);
});
~~~

Сначала сравниваем длину. Если равны — сравниваем строки.

## Почему `CompareOrdinal`

`string.Compare` учитывает культуру, и результат может отличаться на
разных машинах. `CompareOrdinal` сравнивает коды символов и даёт
стабильный результат.

## Вывод

~~~csharp
Console.WriteLine(string.Join(" ", words));
~~~
