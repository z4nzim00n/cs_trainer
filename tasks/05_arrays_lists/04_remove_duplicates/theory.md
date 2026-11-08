# Разбор задания

## HashSet для проверки

~~~csharp
var seen = new HashSet<int>();
var result = new List<int>();
foreach (int x in numbers)
{
    if (seen.Add(x))
    {
        result.Add(x);
    }
}
~~~

`HashSet.Add` возвращает `true`, если элемента ещё не было. Это одновременно
проверка и добавление.

## Почему не Sort + Distinct

`Distinct()` из LINQ сохраняет порядок первого появления, но требует
`using System.Linq`. `HashSet` показывает, как устроена проверка уникальности.

## Сложность

В среднем `HashSet.Add` работает за `O(1)`, поэтому весь проход — `O(n)`.

## Вывод

~~~csharp
Console.WriteLine(string.Join(" ", result));
~~~
