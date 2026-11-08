@@TASK
section: 08_collections
dir: 01_word_count
num: 8_1
title: CS_08_01. Частота слов
topics: `Dictionary`, `TryGetValue`, сортировка ключей
input: Одна строка со словами
@@DESC
Посчитай, сколько раз встречается каждое слово, и выведи по алфавиту:

~~~text
apple: 2
banana: 1
~~~

Порядок строк должен быть отсортирован по слову.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `apple banana apple` | `apple: 2`<br>`banana: 1` |
| `b a b a b` | `a: 2`<br>`b: 3` |
@@THEORY
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
@@TESTS
| `apple banana apple` | `apple: 2\nbanana: 1\n` |
| `b a b a b` | `a: 2\nb: 3\n` |
| `solo` | `solo: 1\n` |
@@CASES
run_case "apple banana apple" $'apple: 2\nbanana: 1\n'
run_case "b a b a b" $'a: 2\nb: 3\n'
run_case "solo" $'solo: 1\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        // TODO: посчитай частоты и выведи их по алфавиту
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

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

        var keys = new List<string>(counts.Keys);
        keys.Sort();
        foreach (string key in keys)
        {
            Console.WriteLine($"{key}: {counts[key]}");
        }
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        var counts = new Dictionary<string, int>();
        foreach (string word in words)
        {
            // TryGetValue совмещает проверку и чтение значения.
            if (counts.TryGetValue(word, out int count))
            {
                counts[word] = count + 1;
            }
            else
            {
                counts[word] = 1;
            }
        }

        // Dictionary не гарантирует порядок, поэтому ключи сортируются.
        var keys = new List<string>(counts.Keys);
        keys.Sort();
        foreach (string key in keys)
        {
            Console.WriteLine($"{key}: {counts[key]}");
        }
    }
}
@@END

@@TASK
section: 08_collections
dir: 02_dictionary_find
num: 8_2
title: CS_08_02. Поиск в словаре
topics: `Dictionary`, `TryGetValue`, `Not found`
input: `n`, затем `n` строк `ключ значение`, затем ключ для поиска
@@DESC
Загрузи пары в словарь и найди значение по ключу:

~~~text
Found: 7
~~~

Если ключа нет, выведи `Not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`apple 5`<br>`banana 7`<br>`kiwi 3`<br>`banana` | `Found: 7` |
| `2`<br>`a 1`<br>`b 2`<br>`z` | `Not found` |
@@THEORY
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
@@TESTS
| `3\napple 5\nbanana 7\nkiwi 3\nbanana` | `Found: 7\n` |
| `2\na 1\nb 2\nz` | `Not found\n` |
| `0\nkey` | `Not found\n` |
@@CASES
run_case $'3\napple 5\nbanana 7\nkiwi 3\nbanana' $'Found: 7\n'
run_case $'2\na 1\nb 2\nz' $'Not found\n'
run_case $'0\nkey' $'Not found\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var map = new Dictionary<string, int>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            map[parts[0]] = int.Parse(parts[1]);
        }

        string query = Console.ReadLine();

        // TODO: найди значение и выведи Found или Not found
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var map = new Dictionary<string, int>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            map[parts[0]] = int.Parse(parts[1]);
        }

        string query = Console.ReadLine();
        if (map.TryGetValue(query, out int value))
        {
            Console.WriteLine($"Found: {value}");
        }
        else
        {
            Console.WriteLine("Not found");
        }
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var map = new Dictionary<string, int>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            map[parts[0]] = int.Parse(parts[1]);
        }

        string query = Console.ReadLine();

        // TryGetValue безопасно сообщает, есть ли ключ.
        if (map.TryGetValue(query, out int value))
        {
            Console.WriteLine($"Found: {value}");
        }
        else
        {
            Console.WriteLine("Not found");
        }
    }
}
@@END

@@TASK
section: 08_collections
dir: 03_unique_elements
num: 8_3
title: CS_08_03. Уникальные элементы
topics: `HashSet`, `List.Sort`, `string.Join`
input: `n`, затем `n` целых чисел
@@DESC
Выведи количество уникальных чисел и сами числа по возрастанию:

~~~text
Unique: 3
1 2 3
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 1 3 2 1` | `Unique: 3`<br>`1 2 3` |
| `4`<br>`7 7 7 7` | `Unique: 1`<br>`7` |
@@THEORY
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
@@TESTS
| `5\n3 1 3 2 1` | `Unique: 3\n1 2 3\n` |
| `4\n7 7 7 7` | `Unique: 1\n7\n` |
| `5\n5 4 3 2 1` | `Unique: 5\n1 2 3 4 5\n` |
@@CASES
run_case $'5\n3 1 3 2 1' $'Unique: 3\n1 2 3\n'
run_case $'4\n7 7 7 7' $'Unique: 1\n7\n'
run_case $'5\n5 4 3 2 1' $'Unique: 5\n1 2 3 4 5\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: найди уникальные числа, отсортируй и выведи
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        var unique = new HashSet<int>();
        for (int i = 0; i < n; ++i)
        {
            unique.Add(int.Parse(parts[i]));
        }

        var result = new List<int>(unique);
        result.Sort();

        Console.WriteLine($"Unique: {unique.Count}");
        Console.WriteLine(string.Join(" ", result));
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // HashSet сам отбрасывает повторы.
        var unique = new HashSet<int>();
        for (int i = 0; i < n; ++i)
        {
            unique.Add(int.Parse(parts[i]));
        }

        // Порядок HashSet не определён — сортируем копию.
        var result = new List<int>(unique);
        result.Sort();

        Console.WriteLine($"Unique: {unique.Count}");
        Console.WriteLine(string.Join(" ", result));
    }
}
@@END

@@TASK
section: 08_collections
dir: 04_group_by_length
num: 8_4
title: CS_08_04. Группировка по длине
topics: `SortedDictionary`, `List<string>`, группы
input: Одна строка со словами
@@DESC
Сгруппируй слова по длине. Группы идут по возрастанию длины, слова
внутри группы — по алфавиту:

~~~text
3: cat dog sun
8: elephant
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `dog elephant cat sun` | `3: cat dog sun`<br>`8: elephant` |
| `aa b ccc` | `1: b`<br>`2: aa`<br>`3: ccc` |
@@THEORY
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
@@TESTS
| `dog elephant cat sun` | `3: cat dog sun\n8: elephant\n` |
| `aa b ccc` | `1: b\n2: aa\n3: ccc\n` |
| `one two` | `3: one two\n` |
@@CASES
run_case "dog elephant cat sun" $'3: cat dog sun\n8: elephant\n'
run_case "aa b ccc" $'1: b\n2: aa\n3: ccc\n'
run_case "one two" $'3: one two\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        // TODO: сгруппируй слова по длине и выведи группы
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        var groups = new SortedDictionary<int, List<string>>();
        foreach (string word in words)
        {
            if (!groups.ContainsKey(word.Length))
            {
                groups[word.Length] = new List<string>();
            }
            groups[word.Length].Add(word);
        }

        foreach (var pair in groups)
        {
            pair.Value.Sort();
            Console.WriteLine($"{pair.Key}: {string.Join(" ", pair.Value)}");
        }
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);

        // SortedDictionary сразу упорядочивает группы по длине.
        var groups = new SortedDictionary<int, List<string>>();
        foreach (string word in words)
        {
            if (!groups.ContainsKey(word.Length))
            {
                groups[word.Length] = new List<string>();
            }
            groups[word.Length].Add(word);
        }

        foreach (var pair in groups)
        {
            // Внутри группы нужен алфавитный порядок.
            pair.Value.Sort();
            Console.WriteLine($"{pair.Key}: {string.Join(" ", pair.Value)}");
        }
    }
}
@@END

@@TASK
section: 08_collections
dir: 05_invert_map
num: 8_5
title: CS_08_05. Инверсия словаря
topics: `SortedDictionary`, индексатор, пары
input: `n`, затем `n` строк `ключ число`
@@DESC
Поменяй местами ключи и значения и выведи по возрастанию числа:

~~~text
1: a
2: b
3: c
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`a 1`<br>`b 2`<br>`c 3` | `1: a`<br>`2: b`<br>`3: c` |
| `2`<br>`x 10`<br>`y 5` | `5: y`<br>`10: x` |
@@THEORY
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
@@TESTS
| `3\na 1\nb 2\nc 3` | `1: a\n2: b\n3: c\n` |
| `2\nx 10\ny 5` | `5: y\n10: x\n` |
| `1\nonly 42` | `42: only\n` |
@@CASES
run_case $'3\na 1\nb 2\nc 3' $'1: a\n2: b\n3: c\n'
run_case $'2\nx 10\ny 5' $'5: y\n10: x\n'
run_case $'1\nonly 42' $'42: only\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: заполни inverted и выведи пары
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var inverted = new SortedDictionary<int, string>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            inverted[int.Parse(parts[1])] = parts[0];
        }

        foreach (var pair in inverted)
        {
            Console.WriteLine($"{pair.Key}: {pair.Value}");
        }
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // Ключом становится число — SortedDictionary упорядочит по нему.
        var inverted = new SortedDictionary<int, string>();
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            inverted[int.Parse(parts[1])] = parts[0];
        }

        foreach (var pair in inverted)
        {
            Console.WriteLine($"{pair.Key}: {pair.Value}");
        }
    }
}
@@END
