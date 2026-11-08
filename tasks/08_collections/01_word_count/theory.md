# Разбор задания

## Словарь

`Dictionary<TKey, TValue>` хранит пары ключ-значение и ищет по ключу
в среднем за `O(1)`:

~~~csharp
var counts = new Dictionary<string, int>();
foreach (string word in words)
{
    if (counts.TryGetValue(word, out int count))
    {
        counts[word] = count + 1;
    }
    else
    {
        counts[word] = 1;
    }
}
~~~

`TryGetValue` возвращает `true`, если ключ есть, и кладёт значение в
`out`-параметр. Это дешевле, чем `ContainsKey` + индексатор.

## Сортировка ключей

Порядок обхода `Dictionary` не определён. Для стабильного вывода соберите
ключи в список и отсортируйте:

~~~csharp
var keys = new List<string>(counts.Keys);
keys.Sort();
foreach (string key in keys)
{
    Console.WriteLine($"{key}: {counts[key]}");
}
~~~

## Альтернатива

`SortedDictionary<string, int>` сразу хранит ключи отсортированными,
но вставка стоит `O(log n)`.
