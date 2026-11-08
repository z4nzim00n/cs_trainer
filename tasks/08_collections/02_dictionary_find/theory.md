# Разбор задания

## Заполнение

~~~csharp
int n = int.Parse(Console.ReadLine());
var map = new Dictionary<string, int>();
for (int i = 0; i < n; ++i)
{
    string[] parts = Console.ReadLine().Split(' ');
    map[parts[0]] = int.Parse(parts[1]);
}
~~~

Индексатор `map[key] = value` добавляет пару или заменяет значение,
если ключ уже есть.

## Поиск

~~~csharp
string query = Console.ReadLine();
if (map.TryGetValue(query, out int value))
{
    Console.WriteLine($"Found: {value}");
}
else
{
    Console.WriteLine("Not found");
}
~~~

`TryGetValue` не бросает исключение при отсутствии ключа, в отличие от
прямого `map[query]`.

## Сложность

Поиск в среднем `O(1)`. Сравнение ключей `string` идёт по содержимому.

## Крайний случай

При `n = 0` словарь пуст, любой запрос даёт `Not found`.
