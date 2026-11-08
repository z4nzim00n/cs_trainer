@@TASK
section: 13_advanced
dir: 01_generic_max
num: 13_1
title: CS_13_01. Обобщённый максимум
topics: дженерики, `IComparable<T>`, `where`
input: Два целых числа, затем два слова
@@DESC
Опиши обобщённый метод `Max<T>` и примени его к числам и строкам:

~~~text
Max int: 7
Max string: banana
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 7`<br>`apple banana` | `Max int: 7`<br>`Max string: banana` |
@@THEORY
## Зачем дженерики

Один алгоритм должен работать для разных типов. Без дженериков
пришлось бы писать `MaxInt`, `MaxString`, `MaxDouble`.

## Обобщённый метод

~~~csharp
static T Max<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) >= 0 ? a : b;
}
~~~

- `<T>` — параметр типа, задаётся при вызове;
- `where T : IComparable<T>` — ограничение: у `T` обязан быть метод
  `CompareTo`.

## Вызов

~~~csharp
int maxInt = Max(3, 7);
string maxString = Max("apple", "banana");
~~~

Компилятор выводит `T` из аргументов: `int` и `string`.

## Ограничения

Без `where` нельзя вызвать `CompareTo`: компилятор не знает, что у `T`
есть такой метод. `IComparable<T>` — стандартный интерфейс сравнения.

## Осторожно со строками

`CompareTo` для `string` зависит от культуры. Для машинного сравнения
используют `string.CompareOrdinal`.
@@TESTS
| `3 7\napple banana` | `Max int: 7\nMax string: banana\n` |
| `-1 -9\ncat dog` | `Max int: -1\nMax string: dog\n` |
| `5 5\na a` | `Max int: 5\nMax string: a\n` |
@@CASES
run_case $'3 7\napple banana' $'Max int: 7\nMax string: banana\n'
run_case $'-1 -9\ncat dog' $'Max int: -1\nMax string: dog\n'
run_case $'5 5\na a' $'Max int: 5\nMax string: a\n'
@@MAIN
using System;

class Program
{
    static T Max<T>(T a, T b) where T : IComparable<T>
    {
        // TODO: верни больший из двух
        return a;
    }

    static void Main()
    {
        string[] numbers = Console.ReadLine().Split(' ');
        string[] words = Console.ReadLine().Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);

        // TODO: выведи Max int и Max string
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) >= 0 ? a : b;
    }

    static void Main()
    {
        string[] numbers = Console.ReadLine().Split(' ');
        string[] words = Console.ReadLine().Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);

        Console.WriteLine($"Max int: {Max(a, b)}");
        Console.WriteLine($"Max string: {Max(words[0], words[1])}");
    }
}
@@COMMENTED
using System;

class Program
{
    // where T : IComparable<T> разрешает вызывать CompareTo.
    static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) >= 0 ? a : b;
    }

    static void Main()
    {
        string[] numbers = Console.ReadLine().Split(' ');
        string[] words = Console.ReadLine().Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);

        // T выводится из аргументов: int и string.
        Console.WriteLine($"Max int: {Max(a, b)}");
        Console.WriteLine($"Max string: {Max(words[0], words[1])}");
    }
}
@@END

@@TASK
section: 13_advanced
dir: 02_lambda_sort
num: 13_2
title: CS_13_02. Сортировка лямбдой
topics: `Comparison<T>`, лямбда, составной порядок
input: `n`, затем `n` слов
@@DESC
Отсортируй слова по длине, а при равной длине — по алфавиту:

~~~text
4
bbb a cc ab
→ a ab cc bbb
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4`<br>`bbb a cc ab` | `a ab cc bbb` |
| `3`<br>`bb aa c` | `c aa bb` |
@@THEORY
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
@@TESTS
| `4\nbbb a cc ab` | `a ab cc bbb\n` |
| `3\nbb aa c` | `c aa bb\n` |
| `2\nsame same` | `same same\n` |
@@CASES
run_case $'4\nbbb a cc ab' $'a ab cc bbb\n'
run_case $'3\nbb aa c' $'c aa bb\n'
run_case $'2\nsame same' $'same same\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        var words = new List<string>();
        for (int i = 0; i < n; ++i)
        {
            words.Add(parts[i]);
        }

        // TODO: отсортируй по длине, затем по алфавиту
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
        var words = new List<string>();
        for (int i = 0; i < n; ++i)
        {
            words.Add(parts[i]);
        }

        words.Sort((x, y) =>
        {
            int cmp = x.Length.CompareTo(y.Length);
            return cmp != 0 ? cmp : string.CompareOrdinal(x, y);
        });

        Console.WriteLine(string.Join(" ", words));
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
        var words = new List<string>();
        for (int i = 0; i < n; ++i)
        {
            words.Add(parts[i]);
        }

        // Составное сравнение: длина, при равенстве — коды символов.
        words.Sort((x, y) =>
        {
            int cmp = x.Length.CompareTo(y.Length);
            return cmp != 0 ? cmp : string.CompareOrdinal(x, y);
        });

        Console.WriteLine(string.Join(" ", words));
    }
}
@@END

@@TASK
section: 13_advanced
dir: 03_linq_algorithms
num: 13_3
title: CS_13_03. LINQ
topics: `Where`, `Select`, `Sum`, LINQ
input: `n`, затем `n` целых чисел
@@DESC
Найди сумму квадратов чётных чисел:

~~~text
Sum: 56
~~~

Для `1 2 3 4 5 6` чётные — `2 4 6`, квадраты — `4 16 36`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `6`<br>`1 2 3 4 5 6` | `Sum: 56` |
| `3`<br>`1 3 5` | `Sum: 0` |
@@THEORY
## LINQ

LINQ — набор методов-расширений для работы с последовательностями:

~~~csharp
using System.Linq;

int sum = numbers
    .Where(x => x % 2 == 0)
    .Select(x => x * x)
    .Sum();
~~~

## Этапы

| Метод | Что делает |
| --- | --- |
| `Where` | оставляет элементы, подходящие под условие |
| `Select` | преобразует каждый элемент |
| `Sum` | складывает результаты |

Цепочка читается сверху вниз: фильтр, преобразование, свёртка.

## Ленивое выполнение

`Where` и `Select` не вычисляются сразу. Работа начинается при вызове
`Sum`, `ToList`, `Count` и других терминальных методов.

## Эквивалент циклом

~~~csharp
int sum = 0;
foreach (int x in numbers)
{
    if (x % 2 == 0)
    {
        sum += x * x;
    }
}
~~~

LINQ короче, но цикл иногда быстрее и проще для отладки.

## Отрицательные числа

`-2 % 2 == 0`, поэтому `-2` считается чётным. Это ожидаемо.
@@TESTS
| `6\n1 2 3 4 5 6` | `Sum: 56\n` |
| `3\n1 3 5` | `Sum: 0\n` |
| `4\n-2 -1 0 2` | `Sum: 8\n` |
@@CASES
run_case $'6\n1 2 3 4 5 6' $'Sum: 56\n'
run_case $'3\n1 3 5' $'Sum: 0\n'
run_case $'4\n-2 -1 0 2' $'Sum: 8\n'
@@MAIN
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        // TODO: сложи квадраты чётных чисел через LINQ
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int sum = numbers
            .Where(x => x % 2 == 0)
            .Select(x => x * x)
            .Sum();

        Console.WriteLine($"Sum: {sum}");
    }
}
@@COMMENTED
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        // Where фильтрует, Select преобразует, Sum сворачивает.
        int sum = numbers
            .Where(x => x % 2 == 0)
            .Select(x => x * x)
            .Sum();

        Console.WriteLine($"Sum: {sum}");
    }
}
@@END

@@TASK
section: 13_advanced
dir: 04_operator_overload
num: 13_4
title: CS_13_04. Перегрузка оператора
topics: `operator +`, `static`, `ToString`
input: Четыре целых числа `x1 y1 x2 y2`
@@DESC
Опиши класс `Vector` и перегрузи `+`, чтобы складывать векторы:

~~~text
1 2 3 4
→ (4, 6)
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1 2 3 4` | `(4, 6)` |
| `-1 5 1 -5` | `(0, 0)` |
@@THEORY
## Перегрузка оператора

Оператор объявляется как статический метод с ключевым словом `operator`:

~~~csharp
class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    public static Vector operator +(Vector a, Vector b)
    {
        return new Vector(a.X + b.X, a.Y + b.Y);
    }
}
~~~

## Вызов

~~~csharp
Vector c = a + b;
~~~

Компилятор превращает это в `Vector.op_Addition(a, b)`.

## Правила

- Хотя бы один параметр должен быть типом, в котором объявлен оператор.
- Нельзя изменить смысл встроенных операторов для встроенных типов.
- Операторы `==` и `!=` перегружают парой, иначе ошибка компиляции.

## Вывод

~~~csharp
Console.WriteLine($"{c.X}, {c.Y}");
~~~

Можно переопределить `ToString()` и печатать объект целиком.
@@TESTS
| `1 2 3 4` | `(4, 6)\n` |
| `-1 5 1 -5` | `(0, 0)\n` |
| `0 0 0 0` | `(0, 0)\n` |
@@CASES
run_case "1 2 3 4" $'(4, 6)\n'
run_case "-1 5 1 -5" $'(0, 0)\n'
run_case "0 0 0 0" $'(0, 0)\n'
@@MAIN
using System;

class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    // TODO: перегрузи оператор +
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Vector a = new Vector(int.Parse(parts[0]), int.Parse(parts[1]));
        Vector b = new Vector(int.Parse(parts[2]), int.Parse(parts[3]));

        // TODO: сложи векторы и выведи результат
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    public static Vector operator +(Vector a, Vector b)
    {
        return new Vector(a.X + b.X, a.Y + b.Y);
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Vector a = new Vector(int.Parse(parts[0]), int.Parse(parts[1]));
        Vector b = new Vector(int.Parse(parts[2]), int.Parse(parts[3]));

        Vector c = a + b;
        Console.WriteLine(c);
    }
}
@@COMMENTED
using System;

class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    // operator + — обычный статический метод с особым именем.
    public static Vector operator +(Vector a, Vector b)
    {
        return new Vector(a.X + b.X, a.Y + b.Y);
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Vector a = new Vector(int.Parse(parts[0]), int.Parse(parts[1]));
        Vector b = new Vector(int.Parse(parts[2]), int.Parse(parts[3]));

        Vector c = a + b;
        Console.WriteLine(c);
    }
}
@@END
