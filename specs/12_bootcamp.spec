@@TASK
section: 12_bootcamp
dir: 01_prime_check
num: 12_1
title: CS_12_01. Простое число
topics: цикл, `%`, `Math.Sqrt`, `bool`
input: Целое число `n`
@@DESC
Определи, является ли число простым:

~~~text
True
~~~

Выведи `True` или `False`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `7` | `True` |
| `9` | `False` |
| `1` | `False` |
@@THEORY
## Определение

Простое число больше `1` и делится только на `1` и на себя.

## Проверка делителей

~~~csharp
static bool IsPrime(int n)
{
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0) return false;
    }
    return true;
}
~~~

Достаточно проверить делители до `√n`: если у числа есть делитель
больше корня, то парный ему делитель меньше корня.

## Почему `i * i <= n`

Условие равносильно `i <= Math.Sqrt(n)`, но без вычисления корня и
дробных чисел. Для очень больших `n` `i * i` может переполниться —
тогда используют `i <= n / i`.

## Крайние случаи

- `n < 2` — не простое;
- `2` — единственное чётное простое;
- отрицательные числа не простые.
@@TESTS
| `7` | `True\n` |
| `9` | `False\n` |
| `1` | `False\n` |
| `2` | `True\n` |
| `13` | `True\n` |
@@CASES
run_case "7" $'True\n'
run_case "9" $'False\n'
run_case "1" $'False\n'
run_case "2" $'True\n'
run_case "13" $'True\n'
@@MAIN
using System;

class Program
{
    static bool IsPrime(int n)
    {
        // TODO: проверь, простое ли число
        return false;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: выведи True или False
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static bool IsPrime(int n)
    {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; ++i)
        {
            if (n % i == 0) return false;
        }
        return true;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(IsPrime(n));
    }
}
@@COMMENTED
using System;

class Program
{
    static bool IsPrime(int n)
    {
        if (n < 2) return false;

        // Проверяем делители до корня включительно.
        for (int i = 2; i * i <= n; ++i)
        {
            if (n % i == 0) return false;
        }
        return true;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(IsPrime(n));
    }
}
@@END

@@TASK
section: 12_bootcamp
dir: 02_coffee_machine
num: 12_2
title: CS_12_02. Кофейный автомат
topics: состояние, команды, `if`/`else`
input: `n`, затем `n` команд
@@DESC
Автомат принимает команды:

- `water X` — добавить `X` воды;
- `coffee X` — добавить `X` кофе;
- `cup` — приготовить чашку, если есть хотя бы `200` воды и `10` кофе.

На `cup` выведи `Coffee ready` или `Not enough resources`. В конце
напечатай остатки:

~~~text
Coffee ready
Not enough resources
Water: 100
Coffee: 10
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`water 500`<br>`coffee 30`<br>`cup`<br>`cup`<br>`cup` | `Coffee ready`<br>`Coffee ready`<br>`Not enough resources`<br>`Water: 100`<br>`Coffee: 10` |
| `3`<br>`water 200`<br>`coffee 10`<br>`cup` | `Coffee ready`<br>`Water: 0`<br>`Coffee: 0` |
@@THEORY
## Состояние

Достаточно двух переменных:

~~~csharp
int water = 0;
int coffee = 0;
~~~

Команды меняют состояние, `cup` проверяет и уменьшает ресурсы.

## Разбор команды

~~~csharp
string[] parts = Console.ReadLine().Split(' ');
if (parts[0] == "water")
{
    water += int.Parse(parts[1]);
}
else if (parts[0] == "coffee")
{
    coffee += int.Parse(parts[1]);
}
else if (parts[0] == "cup")
{
    // ...
}
~~~

## Приготовление

~~~csharp
if (water >= 200 && coffee >= 10)
{
    water -= 200;
    coffee -= 10;
    Console.WriteLine("Coffee ready");
}
else
{
    Console.WriteLine("Not enough resources");
}
~~~

Проверка идёт **до** списания: при нехватке ресурсы не меняются.

## Итог

После всех команд печатаются остатки в формате `Water: X` и
`Coffee: Y`.
@@TESTS
| `5\nwater 500\ncoffee 30\ncup\ncup\ncup` | `Coffee ready\nCoffee ready\nNot enough resources\nWater: 100\nCoffee: 10\n` |
| `3\nwater 200\ncoffee 10\ncup` | `Coffee ready\nWater: 0\nCoffee: 0\n` |
| `4\nwater 199\ncoffee 10\ncup\ncup` | `Not enough resources\nNot enough resources\nWater: 199\nCoffee: 10\n` |
@@CASES
run_case $'5\nwater 500\ncoffee 30\ncup\ncup\ncup' $'Coffee ready\nCoffee ready\nNot enough resources\nWater: 100\nCoffee: 10\n'
run_case $'3\nwater 200\ncoffee 10\ncup' $'Coffee ready\nWater: 0\nCoffee: 0\n'
run_case $'4\nwater 199\ncoffee 10\ncup\ncup' $'Not enough resources\nNot enough resources\nWater: 199\nCoffee: 10\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int water = 0;
        int coffee = 0;

        // TODO: обработай n команд
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int water = 0;
        int coffee = 0;

        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            if (parts[0] == "water")
            {
                water += int.Parse(parts[1]);
            }
            else if (parts[0] == "coffee")
            {
                coffee += int.Parse(parts[1]);
            }
            else if (parts[0] == "cup")
            {
                if (water >= 200 && coffee >= 10)
                {
                    water -= 200;
                    coffee -= 10;
                    Console.WriteLine("Coffee ready");
                }
                else
                {
                    Console.WriteLine("Not enough resources");
                }
            }
        }

        Console.WriteLine($"Water: {water}");
        Console.WriteLine($"Coffee: {coffee}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int water = 0;
        int coffee = 0;

        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            if (parts[0] == "water")
            {
                water += int.Parse(parts[1]);
            }
            else if (parts[0] == "coffee")
            {
                coffee += int.Parse(parts[1]);
            }
            else if (parts[0] == "cup")
            {
                // Сначала проверка, потом списание.
                if (water >= 200 && coffee >= 10)
                {
                    water -= 200;
                    coffee -= 10;
                    Console.WriteLine("Coffee ready");
                }
                else
                {
                    Console.WriteLine("Not enough resources");
                }
            }
        }

        Console.WriteLine($"Water: {water}");
        Console.WriteLine($"Coffee: {coffee}");
    }
}
@@END

@@TASK
section: 12_bootcamp
dir: 03_statistics
num: 12_3
title: CS_12_03. Статистика
topics: минимум, максимум, сумма, среднее, `F2`
input: `n`, затем `n` целых чисел
@@DESC
Выведи минимум, максимум, сумму и среднее:

~~~text
Min: 1
Max: 5
Sum: 15
Average: 3.00
~~~

Среднее — с двумя знаками после точки.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `Min: 1`<br>`Max: 5`<br>`Sum: 15`<br>`Average: 3.00` |
| `3`<br>`2 4 9` | `Min: 2`<br>`Max: 9`<br>`Sum: 15`<br>`Average: 5.00` |
@@THEORY
## Один проход

Все четыре значения можно найти за один цикл:

~~~csharp
int min = int.MaxValue;
int max = int.MinValue;
long sum = 0;
foreach (int x in numbers)
{
    if (x < min) min = x;
    if (x > max) max = x;
    sum += x;
}
double average = (double)sum / n;
~~~

## Среднее

Приведение к `double` обязательно, иначе `sum / n` отбросит дробную
часть.

## Формат

~~~csharp
using System.Globalization;
...
average.ToString("F2", CultureInfo.InvariantCulture)
~~~

`F2` — ровно два знака. `InvariantCulture` печатает точку.

## Пустой список

При `n = 0` минимум, максимум и среднее не определены. В задаче `n > 0`.
@@TESTS
| `5\n1 2 3 4 5` | `Min: 1\nMax: 5\nSum: 15\nAverage: 3.00\n` |
| `3\n2 4 9` | `Min: 2\nMax: 9\nSum: 15\nAverage: 5.00\n` |
| `1\n-5` | `Min: -5\nMax: -5\nSum: -5\nAverage: -5.00\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'Min: 1\nMax: 5\nSum: 15\nAverage: 3.00\n'
run_case $'3\n2 4 9' $'Min: 2\nMax: 9\nSum: 15\nAverage: 5.00\n'
run_case $'1\n-5' $'Min: -5\nMax: -5\nSum: -5\nAverage: -5.00\n'
@@MAIN
using System;
using System.Globalization;

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

        // TODO: найди Min, Max, Sum и Average
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Globalization;

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

        int min = int.MaxValue;
        int max = int.MinValue;
        long sum = 0;
        for (int i = 0; i < n; ++i)
        {
            int x = numbers[i];
            if (x < min) min = x;
            if (x > max) max = x;
            sum += x;
        }

        double average = (double)sum / n;
        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@COMMENTED
using System;
using System.Globalization;

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

        int min = int.MaxValue;
        int max = int.MinValue;
        long sum = 0;
        for (int i = 0; i < n; ++i)
        {
            int x = numbers[i];
            if (x < min) min = x;
            if (x > max) max = x;
            sum += x;
        }

        // (double) обязателен для дробного среднего.
        double average = (double)sum / n;
        Console.WriteLine($"Min: {min}");
        Console.WriteLine($"Max: {max}");
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@END

@@TASK
section: 12_bootcamp
dir: 04_histogram
num: 12_4
title: CS_12_04. Гистограмма
topics: `SortedDictionary`, `new string`, подсчёт
input: `n`, затем `n` чисел от `0` до `9`
@@DESC
Построй гистограмму: для каждого встретившегося значения выведи его и
столько звёздочек, сколько раз оно встретилось. Значения — по возрастанию:

~~~text
2: ***
5: **
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`2 5 2 2 5` | `2: ***`<br>`5: **` |
| `3`<br>`0 9 0` | `0: **`<br>`9: *` |
@@THEORY
## Подсчёт

~~~csharp
var counts = new SortedDictionary<int, int>();
foreach (int x in numbers)
{
    if (counts.ContainsKey(x))
    {
        counts[x]++;
    }
    else
    {
        counts[x] = 1;
    }
}
~~~

`SortedDictionary` хранит значения по возрастанию, поэтому вывод сразу
упорядочен.

## Повторение строки

~~~csharp
string stars = new string('*', counts[value]);
Console.WriteLine($"{value}: {stars}");
~~~

`new string(char, count)` создаёт строку из повторённого символа — это
быстрее, чем конкатенация в цикле.

## Только встретившиеся значения

Мы не печатаем нулевые строки для отсутствующих цифр. Если нужна
фиксированная шкала `0..9`, цикл идёт по всем десяти значениям и
печатает пустую строку звёзд.

## Сложность

Подсчёт `O(n log 10)`, фактически `O(n)`: различных цифр не больше
десяти.
@@TESTS
| `5\n2 5 2 2 5` | `2: ***\n5: **\n` |
| `3\n0 9 0` | `0: **\n9: *\n` |
| `1\n7` | `7: *\n` |
@@CASES
run_case $'5\n2 5 2 2 5' $'2: ***\n5: **\n'
run_case $'3\n0 9 0' $'0: **\n9: *\n'
run_case $'1\n7' $'7: *\n'
@@MAIN
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: посчитай частоты и нарисуй звёздочки
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

        var counts = new SortedDictionary<int, int>();
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (counts.ContainsKey(value))
            {
                counts[value]++;
            }
            else
            {
                counts[value] = 1;
            }
        }

        foreach (var pair in counts)
        {
            string stars = new string('*', pair.Value);
            Console.WriteLine($"{pair.Key}: {stars}");
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
        string[] parts = Console.ReadLine().Split(' ');

        // SortedDictionary сразу сортирует значения.
        var counts = new SortedDictionary<int, int>();
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (counts.ContainsKey(value))
            {
                counts[value]++;
            }
            else
            {
                counts[value] = 1;
            }
        }

        foreach (var pair in counts)
        {
            // new string повторяет символ нужное число раз.
            string stars = new string('*', pair.Value);
            Console.WriteLine($"{pair.Key}: {stars}");
        }
    }
}
@@END

@@TASK
section: 12_bootcamp
dir: 05_rotate_matrix
num: 12_5
title: CS_12_05. Поворот матрицы
topics: двумерный массив, индексы
input: `n`, затем `n` строк по `n` чисел
@@DESC
Поверни квадратную матрицу на 90° по часовой стрелке и выведи её:

~~~text
2
1 2
3 4
→ 3 1
  4 2
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2`<br>`1 2`<br>`3 4` | `3 1`<br>`4 2` |
| `1`<br>`7` | `7` |
@@THEORY
## Куда переходит элемент

При повороте на 90° по часовой стрелке элемент `a[i, j]` встаёт в
позицию `b[j, n - 1 - i]`.

Обратная формула, удобная для заполнения результата:

~~~text
b[i, j] = a[n - 1 - j, i]
~~~

## Код

~~~csharp
int[,] b = new int[n, n];
for (int i = 0; i < n; ++i)
{
    for (int j = 0; j < n; ++j)
    {
        b[i, j] = a[n - 1 - j, i];
    }
}
~~~

## Вывод

~~~csharp
for (int i = 0; i < n; ++i)
{
    string[] row = new string[n];
    for (int j = 0; j < n; ++j)
    {
        row[j] = b[i, j].ToString();
    }
    Console.WriteLine(string.Join(" ", row));
}
~~~

## Трассировка 2×2

| Элемент | Позиция после поворота |
| --- | --- |
| `a[0,0] = 1` | `b[0,1]` |
| `a[0,1] = 2` | `b[1,1]` |
| `a[1,0] = 3` | `b[0,0]` |
| `a[1,1] = 4` | `b[1,0]` |

Результат: `3 1` / `4 2`.
@@TESTS
| `2\n1 2\n3 4` | `3 1\n4 2\n` |
| `3\n1 2 3\n4 5 6\n7 8 9` | `7 4 1\n8 5 2\n9 6 3\n` |
| `1\n7` | `7\n` |
@@CASES
run_case $'2\n1 2\n3 4' $'3 1\n4 2\n'
run_case $'3\n1 2 3\n4 5 6\n7 8 9' $'7 4 1\n8 5 2\n9 6 3\n'
run_case $'1\n7' $'7\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        // TODO: поверни матрицу и выведи строки
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        for (int i = 0; i < n; ++i)
        {
            string[] row = new string[n];
            for (int j = 0; j < n; ++j)
            {
                row[j] = a[n - 1 - j, i].ToString();
            }
            Console.WriteLine(string.Join(" ", row));
        }
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        for (int i = 0; i < n; ++i)
        {
            string[] row = new string[n];
            for (int j = 0; j < n; ++j)
            {
                // Столбец снизу вверх становится строкой слева направо.
                row[j] = a[n - 1 - j, i].ToString();
            }
            Console.WriteLine(string.Join(" ", row));
        }
    }
}
@@END

@@TASK
section: 12_bootcamp
dir: 06_matrix_sum
num: 12_6
title: CS_12_06. Сумма и диагональ
topics: двумерный массив, вложенные циклы
input: `n`, затем `n` строк по `n` чисел
@@DESC
Выведи сумму всех элементов и сумму главной диагонали:

~~~text
Sum: 10
Diagonal: 5
~~~

Главная диагональ — элементы `a[i, i]`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2`<br>`1 2`<br>`3 4` | `Sum: 10`<br>`Diagonal: 5` |
| `1`<br>`7` | `Sum: 7`<br>`Diagonal: 7` |
@@THEORY
## Двумерный массив

~~~csharp
int[,] a = new int[n, n];
~~~

`a.GetLength(0)` — число строк, `a.GetLength(1)` — число столбцов. У
квадратной матрицы они равны.

## Обход

~~~csharp
long sum = 0;
long diagonal = 0;
for (int i = 0; i < n; ++i)
{
    for (int j = 0; j < n; ++j)
    {
        sum += a[i, j];
        if (i == j)
        {
            diagonal += a[i, j];
        }
    }
}
~~~

## Диагональ отдельным циклом

~~~csharp
for (int i = 0; i < n; ++i)
{
    diagonal += a[i, i];
}
~~~

Так короче, но тогда по матрице два прохода вместо одного.

## Тип суммы

`long` защищает от переполнения, если элементов много, а значения
большие.

## Порядок вывода

Сначала `Sum`, затем `Diagonal` — ровно так, как в примере.
@@TESTS
| `2\n1 2\n3 4` | `Sum: 10\nDiagonal: 5\n` |
| `3\n1 2 3\n4 5 6\n7 8 9` | `Sum: 45\nDiagonal: 15\n` |
| `1\n7` | `Sum: 7\nDiagonal: 7\n` |
@@CASES
run_case $'2\n1 2\n3 4' $'Sum: 10\nDiagonal: 5\n'
run_case $'3\n1 2 3\n4 5 6\n7 8 9' $'Sum: 45\nDiagonal: 15\n'
run_case $'1\n7' $'Sum: 7\nDiagonal: 7\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        // TODO: посчитай Sum и Diagonal и выведи их
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        long sum = 0;
        long diagonal = 0;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                sum += a[i, j];
                if (i == j)
                {
                    diagonal += a[i, j];
                }
            }
        }

        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Diagonal: {diagonal}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] a = new int[n, n];
        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            for (int j = 0; j < n; ++j)
            {
                a[i, j] = int.Parse(parts[j]);
            }
        }

        long sum = 0;
        long diagonal = 0;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                sum += a[i, j];
                // Элементы главной диагонали лежат там, где i == j.
                if (i == j)
                {
                    diagonal += a[i, j];
                }
            }
        }

        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Diagonal: {diagonal}");
    }
}
@@END
