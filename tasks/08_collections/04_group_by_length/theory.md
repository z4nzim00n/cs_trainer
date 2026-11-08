# Разбор задания

## Словарь списков

Группировка — это `Dictionary<int, List<string>>`:

~~~csharp
var groups = new SortedDictionary<int, List<string>>();
foreach (string word in words)
{
    if (!groups.ContainsKey(word.Length))
    {
        groups[word.Length] = new List<string>();
    }
    groups[word.Length].Add(word);
}
~~~

`SortedDictionary` хранит ключи по возрастанию, поэтому группы сразу
идут в нужном порядке.

## Сортировка внутри группы

~~~csharp
foreach (var pair in groups)
{
    pair.Value.Sort();
    Console.WriteLine($"{pair.Key}: {string.Join(" ", pair.Value)}");
}
~~~

`Sort()` у `List<string>` сравнивает строки по алфавиту.

## Почему не группировка LINQ

`GroupBy` короче, но возвращает `IGrouping`, порядок ключей нужно
обеспечивать отдельно. Явный словарь показывает устройство группировки.

## Сложность

Вставка в `SortedDictionary` — `O(log g)`, где `g` — число групп.
Сортировка каждого списка — `O(m log m)`.
