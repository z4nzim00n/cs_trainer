@@TASK
section: 05_arrays_lists
dir: 01_list_sum_average
num: 5_1
title: CS_05_01. Сумма и среднее
topics: `List<int>`, `for`, среднее, `F2`
input: `n`, затем `n` целых чисел
@@DESC
Найди сумму и среднее арифметическое списка:

~~~text
Sum: 15
Average: 3.00
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `Sum: 15`<br>`Average: 3.00` |
| `3`<br>`2 4 9` | `Sum: 15`<br>`Average: 5.00` |
@@THEORY
## Список

~~~csharp
var numbers = new List<int>();
for (int i = 0; i < n; ++i)
{
    numbers.Add(int.Parse(parts[i]));
}
~~~

`List<int>` — динамический массив. В отличие от `int[]`, его размер можно
увеличивать через `Add`.

## Сумма

~~~csharp
long sum = 0;
foreach (int x in numbers)
{
    sum += x;
}
~~~

`long` защищает от переполнения при больших значениях.

## Среднее

~~~csharp
double average = (double)sum / n;
~~~

Приведение к `double` обязательно: `sum / n` для целых даст целое число.

## Формат

~~~csharp
Console.WriteLine("Sum: " + sum);
Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
~~~

## Пустой список

При `n = 0` среднее не определено. В задаче `n > 0`.
@@TESTS
| `5\n1 2 3 4 5` | `Sum: 15\nAverage: 3.00\n` |
| `3\n2 4 9` | `Sum: 15\nAverage: 5.00\n` |
| `1\n7` | `Sum: 7\nAverage: 7.00\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'Sum: 15\nAverage: 3.00\n'
run_case $'3\n2 4 9' $'Sum: 15\nAverage: 5.00\n'
run_case $'1\n7' $'Sum: 7\nAverage: 7.00\n'
@@MAIN
using System;
using System.Collections.Generic;
using System.Globalization;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // TODO: выведи Sum и Average
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Collections.Generic;
using System.Globalization;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        long sum = 0;
        foreach (int x in numbers)
        {
            sum += x;
        }

        double average = (double)sum / n;
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@COMMENTED
using System;
using System.Collections.Generic;
using System.Globalization;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        long sum = 0;
        foreach (int x in numbers)
        {
            sum += x;
        }

        // Приводим sum к double, иначе деление будет целочисленным.
        double average = (double)sum / n;
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@END

@@TASK
section: 05_arrays_lists
dir: 02_min_max
num: 5_2
title: CS_05_02. Минимум и максимум
topics: `List<int>`, `int.MinValue`, `int.MaxValue`
input: `n`, затем `n` целых чисел
@@DESC
Найди минимальное и максимальное значения:

~~~text
Min: 1
Max: 9
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`4 9 1 7 3` | `Min: 1`<br>`Max: 9` |
| `3`<br>`-5 -2 -8` | `Min: -8`<br>`Max: -2` |
@@THEORY
## Начальные значения

~~~csharp
int min = int.MaxValue;
int max = int.MinValue;
~~~

`int.MaxValue` больше любого `int`, поэтому первое число станет минимумом.
`int.MinValue` наоборот станет максимумом.

## Один проход

~~~csharp
foreach (int x in numbers)
{
    if (x < min) min = x;
    if (x > max) max = x;
}
~~~

Оба значения находятся за один проход, без сортировки.

## Альтернативы

- `numbers.Min()` и `numbers.Max()` из LINQ — короче, но требует `using System.Linq`.
- Сортировка и взятие первого/последнего — `O(n log n)` вместо `O(n)`.

## Крайние случаи

Для пустого списка минимум и максимум не определены. В задаче `n > 0`.
@@TESTS
| `5\n4 9 1 7 3` | `Min: 1\nMax: 9\n` |
| `3\n-5 -2 -8` | `Min: -8\nMax: -2\n` |
| `1\n42` | `Min: 42\nMax: 42\n` |
@@CASES
run_case $'5\n4 9 1 7 3' $'Min: 1\nMax: 9\n'
run_case $'3\n-5 -2 -8' $'Min: -8\nMax: -2\n'
run_case $'1\n42' $'Min: 42\nMax: 42\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // TODO: найди Min и Max и выведи их
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        int min = int.MaxValue;
        int max = int.MinValue;
        foreach (int x in numbers)
        {
            if (x < min) min = x;
            if (x > max) max = x;
        }

        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // Начальные значения — крайние представимые числа int.
        int min = int.MaxValue;
        int max = int.MinValue;
        foreach (int x in numbers)
        {
            if (x < min) min = x;
            if (x > max) max = x;
        }

        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
    }
}
@@END

@@TASK
section: 05_arrays_lists
dir: 03_reverse_list
num: 5_3
title: CS_05_03. Разворот списка
topics: `List<int>`, `Reverse`, `string.Join`
input: `n`, затем `n` целых чисел
@@DESC
Выведи числа в обратном порядке через пробел:

~~~text
5
1 2 3 4 5
→ 5 4 3 2 1
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `5 4 3 2 1` |
| `3`<br>`10 20 30` | `30 20 10` |
@@THEORY
## Разворот списка

~~~csharp
numbers.Reverse();
~~~

`List<T>.Reverse()` меняет порядок элементов на месте.

## Вывод через пробел

~~~csharp
Console.WriteLine(string.Join(" ", numbers));
~~~

`string.Join` превращает элементы в строки и соединяет разделителем.
Для `List<int>` есть перегрузка, принимающая `IEnumerable<T>`.

## Разворот без изменения

Если исходный порядок нужен дальше, идите с конца:

~~~csharp
for (int i = numbers.Count - 1; i >= 0; --i)
{
    // ...
}
~~~

## Пустой список

`string.Join` вернёт пустую строку, `WriteLine` напечатает пустую строку.
В задаче `n > 0`.
@@TESTS
| `5\n1 2 3 4 5` | `5 4 3 2 1\n` |
| `3\n10 20 30` | `30 20 10\n` |
| `1\n7` | `7\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'5 4 3 2 1\n'
run_case $'3\n10 20 30' $'30 20 10\n'
run_case $'1\n7' $'7\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // TODO: разверни список и выведи числа через пробел
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        numbers.Reverse();
        Console.WriteLine(string.Join(" ", numbers));
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // Reverse меняет порядок на месте.
        numbers.Reverse();
        Console.WriteLine(string.Join(" ", numbers));
    }
}
@@END

@@TASK
section: 05_arrays_lists
dir: 04_remove_duplicates
num: 5_4
title: CS_05_04. Убрать дубликаты
topics: `HashSet<int>`, `List<int>`, порядок элементов
input: `n`, затем `n` целых чисел
@@DESC
Оставь только первое вхождение каждого числа, сохранив исходный порядок:

~~~text
7
1 2 1 3 2 4 1
→ 1 2 3 4
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `7`<br>`1 2 1 3 2 4 1` | `1 2 3 4` |
| `4`<br>`5 5 5 5` | `5` |
@@THEORY
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
@@TESTS
| `7\n1 2 1 3 2 4 1` | `1 2 3 4\n` |
| `4\n5 5 5 5` | `5\n` |
| `3\n3 2 1` | `3 2 1\n` |
@@CASES
run_case $'7\n1 2 1 3 2 4 1' $'1 2 3 4\n'
run_case $'4\n5 5 5 5' $'5\n'
run_case $'3\n3 2 1' $'3 2 1\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // TODO: убери повторы, сохранив порядок, и выведи результат
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        var seen = new HashSet<int>();
        var result = new List<int>();
        foreach (int x in numbers)
        {
            if (seen.Add(x))
            {
                result.Add(x);
            }
        }

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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // Add возвращает false, если число уже встречалось.
        var seen = new HashSet<int>();
        var result = new List<int>();
        foreach (int x in numbers)
        {
            if (seen.Add(x))
            {
                result.Add(x);
            }
        }

        Console.WriteLine(string.Join(" ", result));
    }
}
@@END

@@TASK
section: 05_arrays_lists
dir: 05_sort_numbers
num: 5_5
title: CS_05_05. Сортировка
topics: `List.Sort`, `string.Join`
input: `n`, затем `n` целых чисел
@@DESC
Отсортируй числа по возрастанию и выведи через пробел:

~~~text
5
3 1 4 2 5
→ 1 2 3 4 5
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 1 4 2 5` | `1 2 3 4 5` |
| `4`<br>`10 -1 3 0` | `-1 0 3 10` |
@@THEORY
## Сортировка списка

~~~csharp
numbers.Sort();
~~~

`List<int>.Sort()` сортирует по возрастанию. Для `int` используется
стандартное сравнение.

## Сортировка массива

~~~csharp
Array.Sort(array);
~~~

Для массива вызывается статический метод `Array.Sort`.

## Компаратор

Для другого порядка передайте `Comparison<T>`:

~~~csharp
numbers.Sort((a, b) => b.CompareTo(a)); // по убыванию
~~~

Лямбда возвращает отрицательное число, ноль или положительное — как
`CompareTo`.

## Вывод

~~~csharp
Console.WriteLine(string.Join(" ", numbers));
~~~
@@TESTS
| `5\n3 1 4 2 5` | `1 2 3 4 5\n` |
| `4\n10 -1 3 0` | `-1 0 3 10\n` |
| `1\n42` | `42\n` |
@@CASES
run_case $'5\n3 1 4 2 5' $'1 2 3 4 5\n'
run_case $'4\n10 -1 3 0' $'-1 0 3 10\n'
run_case $'1\n42' $'42\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // TODO: отсортируй список и выведи числа через пробел
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        numbers.Sort();
        Console.WriteLine(string.Join(" ", numbers));
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
        var numbers = new List<int>();
        for (int i = 0; i < n; ++i)
        {
            numbers.Add(int.Parse(parts[i]));
        }

        // Sort без аргументов сортирует по возрастанию.
        numbers.Sort();
        Console.WriteLine(string.Join(" ", numbers));
    }
}
@@END

@@TASK
section: 05_arrays_lists
dir: 06_rotate_list
num: 5_6
title: CS_05_06. Циклический сдвиг
topics: `%`, индексы, новый массив
input: `n`, `k`, затем `n` целых чисел
@@DESC
Сдвинь список вправо на `k` позиций и выведи через пробел:

~~~text
5 2
1 2 3 4 5
→ 4 5 1 2 3
~~~

`k` может быть больше `n`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5 2`<br>`1 2 3 4 5` | `4 5 1 2 3` |
| `4 0`<br>`1 2 3 4` | `1 2 3 4` |
| `3 5`<br>`1 2 3` | `2 3 1` |
@@THEORY
## Приведение сдвига

~~~csharp
k = k % n;
~~~

Если сдвинуть на `n` позиций, список вернётся в исходное состояние. Поэтому
достаточно `k % n`.

## Куда встанет элемент

~~~csharp
int[] result = new int[n];
for (int i = 0; i < n; ++i)
{
    result[(i + k) % n] = numbers[i];
}
~~~

Элемент с индексом `i` переходит в `(i + k) % n`.

## Трассировка

Для `[1,2,3,4,5]`, `k = 2`:

| i | значение | новый индекс |
| --- | --- | --- |
| 0 | 1 | 2 |
| 1 | 2 | 3 |
| 2 | 3 | 4 |
| 3 | 4 | 0 |
| 4 | 5 | 1 |

Результат: `4 5 1 2 3`.

## Пустой список

При `n = 0` деление на ноль в `k % n` недопустимо. В задаче `n > 0`.
@@TESTS
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `4 0\n1 2 3 4` | `1 2 3 4\n` |
| `3 5\n1 2 3` | `2 3 1\n` |
@@CASES
run_case $'5 2\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'4 0\n1 2 3 4' $'1 2 3 4\n'
run_case $'3 5\n1 2 3' $'2 3 1\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] header = Console.ReadLine().Split(' ');
        int n = int.Parse(header[0]);
        int k = int.Parse(header[1]);
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: сдвинь числа вправо на k и выведи через пробел
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string[] header = Console.ReadLine().Split(' ');
        int n = int.Parse(header[0]);
        int k = int.Parse(header[1]);
        string[] parts = Console.ReadLine().Split(' ');

        k = k % n;
        int[] result = new int[n];
        for (int i = 0; i < n; ++i)
        {
            result[(i + k) % n] = int.Parse(parts[i]);
        }

        Console.WriteLine(string.Join(" ", result));
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string[] header = Console.ReadLine().Split(' ');
        int n = int.Parse(header[0]);
        int k = int.Parse(header[1]);
        string[] parts = Console.ReadLine().Split(' ');

        // Сдвиг на n возвращает исходный порядок, поэтому берём остаток.
        k = k % n;
        int[] result = new int[n];
        for (int i = 0; i < n; ++i)
        {
            result[(i + k) % n] = int.Parse(parts[i]);
        }

        Console.WriteLine(string.Join(" ", result));
    }
}
@@END
