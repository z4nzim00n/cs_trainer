@@TASK
section: 03_expressions
dir: 01_circle_area
num: 3_1
title: CS_03_01. Площадь круга
topics: `double`, `Math.PI`, форматирование `F2`
input: Радиус круга
@@DESC
Считай радиус и выведи площадь круга с двумя знаками после точки:

~~~text
Area: 12.57
~~~

Формула: `S = π · r²`. Используй `Math.PI`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2` | `Area: 12.57` |
| `1` | `Area: 3.14` |
@@THEORY
## Формула

~~~csharp
double area = Math.PI * radius * radius;
~~~

`Math.PI` — константа π с достаточной точностью. `Math.Pow(radius, 2)`
тоже подходит, но умножение проще и быстрее.

## Ввод и вывод

~~~csharp
double radius = double.Parse(line, CultureInfo.InvariantCulture);
string text = area.ToString("F2", CultureInfo.InvariantCulture);
Console.WriteLine("Area: " + text);
~~~

## Порядок операций

`Math.PI * radius * radius` вычисляется слева направо:
`(π · r) · r`. Это то же самое, что `π · r²`.

## Ошибки

- Забыли `InvariantCulture` — на русской Windows получится `12,57`.
- Использовали `float` — точности меньше, но для двух знаков обычно хватает.
- Перепутали радиус и диаметр — площадь отличается в четыре раза.
@@TESTS
| `2` | `Area: 12.57\n` |
| `1` | `Area: 3.14\n` |
| `0.5` | `Area: 0.79\n` |
@@CASES
run_case "2" $'Area: 12.57\n'
run_case "1" $'Area: 3.14\n'
run_case "0.5" $'Area: 0.79\n'
@@MAIN
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radius = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // TODO: вычисли площадь и выведи Area: <площадь с двумя знаками>
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
        double radius = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
        double area = Math.PI * radius * radius;

        Console.WriteLine("Area: " + area.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@COMMENTED
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radius = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // Math.PI — встроенная константа; F2 оставляет два знака.
        double area = Math.PI * radius * radius;
        Console.WriteLine("Area: " + area.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@END

@@TASK
section: 03_expressions
dir: 02_radians_to_degrees
num: 3_2
title: CS_03_02. Радианы в градусы
topics: `double`, `Math.PI`, преобразование величин
input: Угол в радианах
@@DESC
Переведи угол из радиан в градусы и выведи результат с двумя знаками:

~~~text
Degrees: 180.00
~~~

Формула: `градусы = радианы · 180 / π`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3.14159265358979` | `Degrees: 180.00` |
| `1.5707963267949` | `Degrees: 90.00` |
@@THEORY
## Преобразование

~~~csharp
double degrees = radians * 180.0 / Math.PI;
~~~

Порядок важен: сначала умножаем на `180.0`, потом делим на π. Если написать
`radians * (180 / Math.PI)`, результат будет тем же, потому что `180 / Math.PI`
уже дробное.

## Почему 180.0, а не 180

`radians` — `double`, поэтому `radians * 180` тоже `double`. Но запись
`180.0` сразу показывает читателю, что деление дробное.

## Формат

~~~csharp
Console.WriteLine("Degrees: " + degrees.ToString("F2", CultureInfo.InvariantCulture));
~~~

## Точность

`Math.PI` — приближение. При переводе туда и обратно возможна погрешность
в последних знаках. Формат `F2` скрывает её.
@@TESTS
| `3.14159265358979` | `Degrees: 180.00\n` |
| `1.5707963267949` | `Degrees: 90.00\n` |
| `0` | `Degrees: 0.00\n` |
@@CASES
run_case "3.14159265358979" $'Degrees: 180.00\n'
run_case "1.5707963267949" $'Degrees: 90.00\n'
run_case "0" $'Degrees: 0.00\n'
@@MAIN
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radians = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // TODO: переведи радианы в градусы и выведи Degrees: <результат>
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
        double radians = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
        double degrees = radians * 180.0 / Math.PI;

        Console.WriteLine("Degrees: " + degrees.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@COMMENTED
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double radians = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

        // 180 / π — коэффициент перевода радиан в градусы.
        double degrees = radians * 180.0 / Math.PI;
        Console.WriteLine("Degrees: " + degrees.ToString("F2", CultureInfo.InvariantCulture));
    }
}
@@END

@@TASK
section: 03_expressions
dir: 03_digit_swap
num: 3_3
title: CS_03_03. Обмен крайних цифр
topics: `/`, `%`, разряды числа
input: Четырёхзначное целое число
@@DESC
Поменяй местами первую и последнюю цифры четырёхзначного числа.

~~~text
1234 → 4231
~~~

Выведи только результат.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1234` | `4231` |
| `1001` | `1001` |
@@THEORY
## Разряды через деление и остаток

~~~csharp
int thousands = n / 1000;
int hundreds = n / 100 % 10;
int tens = n / 10 % 10;
int units = n % 10;
~~~

`/` отбрасывает дробную часть, `%` даёт остаток.

## Сборка числа

~~~csharp
int result = units * 1000 + hundreds * 100 + tens * 10 + thousands;
~~~

Для `1234`: `4·1000 + 2·100 + 3·10 + 1 = 4231`.

## Проверка

| n | result |
| --- | --- |
| 1234 | 4231 |
| 1001 | 1001 |
| 9876 | 6879 |

## Ограничение

Число должно быть четырёхзначным. Для `100` формула даст `1`, потому что
ведущий ноль не хранится в `int`. В задаче гарантирован диапазон `1000…9999`.
@@TESTS
| `1234` | `4231\n` |
| `1001` | `1001\n` |
| `9876` | `6879\n` |
@@CASES
run_case "1234" $'4231\n'
run_case "1001" $'1001\n'
run_case "9876" $'6879\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: поменяй первую и последнюю цифры, выведи результат
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

        int thousands = n / 1000;
        int middle = n / 10 % 100;
        int units = n % 10;

        int result = units * 1000 + middle * 10 + thousands;
        Console.WriteLine(result);
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // Средние две цифры удобно взять одним куском: n / 10 % 100.
        int thousands = n / 1000;
        int middle = n / 10 % 100;
        int units = n % 10;

        int result = units * 1000 + middle * 10 + thousands;
        Console.WriteLine(result);
    }
}
@@END

@@TASK
section: 03_expressions
dir: 04_integer_division
num: 3_4
title: CS_03_04. Целочисленное деление
topics: `/`, `%`, отрицательные числа
input: Два целых числа `a` и `b`
@@DESC
Выведи частное и остаток от деления `a` на `b`:

~~~text
7 / 2 = 3
7 % 2 = 1
~~~

`b` не равен нулю.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `7 2` | `7 / 2 = 3`<br>`7 % 2 = 1` |
| `-7 2` | `-7 / 2 = -3`<br>`-7 % 2 = -1` |
@@THEORY
## Деление целых

~~~csharp
int quotient = a / b;
int remainder = a % b;
~~~

Если оба операнда `int`, дробная часть отбрасывается к нулю. Для `-7 / 2`
результат `-3`, а остаток `-1`.

## Связь частного и остатка

~~~text
a = b * (a / b) + (a % b)
~~~

Проверка: `-7 = 2 * (-3) + (-1)`.

## Деление на ноль

`a / 0` для целых бросает `DivideByZeroException`. В этой задаче `b ≠ 0`.

## Отличие от double

| Выражение | Результат |
| --- | --- |
| `7 / 2` | `3` |
| `7 / 2.0` | `3.5` |
| `7 % 2` | `1` |
@@TESTS
| `7 2` | `7 / 2 = 3\n7 % 2 = 1\n` |
| `-7 2` | `-7 / 2 = -3\n-7 % 2 = -1\n` |
| `10 5` | `10 / 5 = 2\n10 % 5 = 0\n` |
@@CASES
run_case "7 2" $'7 / 2 = 3\n7 % 2 = 1\n'
run_case "-7 2" $'-7 / 2 = -3\n-7 % 2 = -1\n'
run_case "10 5" $'10 / 5 = 2\n10 % 5 = 0\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // TODO: выведи частное и остаток в формате из условия
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        Console.WriteLine($"{a} / {b} = {a / b}");
        Console.WriteLine($"{a} % {b} = {a % b}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // / даёт частное, % — остаток. Для отрицательных дробная часть
        // отбрасывается к нулю.
        Console.WriteLine($"{a} / {b} = {a / b}");
        Console.WriteLine($"{a} % {b} = {a % b}");
    }
}
@@END

@@TASK
section: 03_expressions
dir: 05_boolean_logic
num: 3_5
title: CS_03_05. Логическое выражение
topics: `bool`, `&&`, `||`, сравнения
input: Возраст и наличие билета (0 или 1)
@@DESC
Человек проходит на мероприятие, если ему `18` лет или больше **и** у него
есть билет. Билет обозначается `1`, его отсутствие — `0`.

Выведи:

~~~text
Allowed: True
~~~

или `Allowed: False`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `20 1` | `Allowed: True` |
| `17 1` | `Allowed: False` |
| `20 0` | `Allowed: False` |
@@THEORY
## Логические операторы

| Оператор | Значение |
| --- | --- |
| `&&` | «и» |
| `\|\|` | «или» |
| `!` | «не» |

~~~csharp
bool allowed = age >= 18 && ticket == 1;
~~~

Оба условия должны быть истинны.

## Короткое замыкание

`&&` не вычисляет правую часть, если левая ложна. Это полезно, когда правая
часть может быть опасной:

~~~csharp
if (items != null && items.Count > 0) { ... }
~~~

## Вывод bool

`Console.WriteLine(allowed)` печатает `True` или `False` с заглавной буквы.
Интерполяция делает то же самое.

## Приоритет

`!` выполняется раньше `&&`, а `&&` — раньше `||`. При сомнениях ставьте
скобки: `(a || b) && c`.
@@TESTS
| `20 1` | `Allowed: True\n` |
| `17 1` | `Allowed: False\n` |
| `20 0` | `Allowed: False\n` |
| `18 1` | `Allowed: True\n` |
@@CASES
run_case "20 1" $'Allowed: True\n'
run_case "17 1" $'Allowed: False\n'
run_case "20 0" $'Allowed: False\n'
run_case "18 1" $'Allowed: True\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        int ticket = int.Parse(parts[1]);

        // TODO: вычисли, проходит ли человек, и выведи Allowed: True/False
        bool allowed = false;
        Console.WriteLine($"Allowed: {allowed}");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        int ticket = int.Parse(parts[1]);

        bool allowed = age >= 18 && ticket == 1;
        Console.WriteLine($"Allowed: {allowed}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        int ticket = int.Parse(parts[1]);

        // Нужны одновременно возраст 18+ и билет.
        bool allowed = age >= 18 && ticket == 1;
        Console.WriteLine($"Allowed: {allowed}");
    }
}
@@END

@@TASK
section: 04_loops
dir: 01_sequence_max
num: 4_1
title: CS_04_01. Максимум последовательности
topics: `for`, `int.MaxValue`, `int.MinValue`
input: `n`, затем `n` целых чисел
@@DESC
Найди максимальное число в последовательности и выведи:

~~~text
Max: <число>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 9 2 7 1` | `Max: 9` |
| `3`<br>`-5 -2 -8` | `Max: -2` |
@@THEORY
## Цикл с накоплением

~~~csharp
int n = int.Parse(Console.ReadLine());
string[] parts = Console.ReadLine().Split(' ');
int max = int.MinValue;
for (int i = 0; i < n; ++i)
{
    int value = int.Parse(parts[i]);
    if (value > max)
    {
        max = value;
    }
}
~~~

`int.MinValue` — самое маленькое число `int`. Любое введённое значение
больше него, поэтому первое число станет начальным максимумом.

## Почему не 0

Если начать с `max = 0`, последовательность из отрицательных чисел даст
неверный ответ `0`. Правильный начальный максимум — `int.MinValue`.

## Вывод

~~~csharp
Console.WriteLine($"Max: {max}");
~~~

## Крайние случаи

`n = 0` в задаче не встречается. Если бы встречался, максимум был бы
не определён и его нужно было бы обработать отдельно.
@@TESTS
| `5\n3 9 2 7 1` | `Max: 9\n` |
| `3\n-5 -2 -8` | `Max: -2\n` |
| `1\n42` | `Max: 42\n` |
@@CASES
run_case $'5\n3 9 2 7 1' $'Max: 9\n'
run_case $'3\n-5 -2 -8' $'Max: -2\n'
run_case $'1\n42' $'Max: 42\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: найди максимум и выведи Max: <число>
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
        string[] parts = Console.ReadLine().Split(' ');

        int max = int.MinValue;
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (value > max)
            {
                max = value;
            }
        }

        Console.WriteLine($"Max: {max}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // MinValue гарантирует, что первое число станет максимумом,
        // даже если все числа отрицательные.
        int max = int.MinValue;
        for (int i = 0; i < n; ++i)
        {
            int value = int.Parse(parts[i]);
            if (value > max)
            {
                max = value;
            }
        }

        Console.WriteLine($"Max: {max}");
    }
}
@@END

@@TASK
section: 04_loops
dir: 02_sum_of_digits
num: 4_2
title: CS_04_02. Сумма цифр
topics: `while`, `% 10`, `/ 10`
input: Неотрицательное целое число
@@DESC
Найди сумму цифр числа:

~~~text
12345 → 15
~~~

Выведи:

~~~text
Sum: 15
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `12345` | `Sum: 15` |
| `0` | `Sum: 0` |
@@THEORY
## Выделение последней цифры

~~~csharp
int digit = n % 10;
n = n / 10;
~~~

`% 10` даёт последнюю цифру, `/ 10` отбрасывает её.

## Цикл

~~~csharp
int sum = 0;
while (n > 0)
{
    sum += n % 10;
    n /= 10;
}
~~~

Для `12345`: цифры `5, 4, 3, 2, 1`, сумма `15`.

## Ноль

Для `n = 0` цикл не выполнится ни разу, и сумма останется `0`. Это правильно.

## Отрицательные числа

Для отрицательного `n` условие `n > 0` сразу ложно. Если нужна сумма цифр
по модулю, используют `Math.Abs(n)` или работают с `long`. В задаче число
неотрицательное.
@@TESTS
| `12345` | `Sum: 15\n` |
| `0` | `Sum: 0\n` |
| `9009` | `Sum: 18\n` |
@@CASES
run_case "12345" $'Sum: 15\n'
run_case "0" $'Sum: 0\n'
run_case "9009" $'Sum: 18\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: посчитай сумму цифр и выведи Sum: <сумма>
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

        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // На каждой итерации отделяем последнюю цифру и убираем её.
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
@@END

@@TASK
section: 04_loops
dir: 03_max_digit
num: 4_3
title: CS_04_03. Максимальная цифра
topics: `while`, цифры числа, сравнение
input: Неотрицательное целое число
@@DESC
Найди максимальную цифру числа и выведи:

~~~text
Max digit: 9
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `9073` | `Max digit: 9` |
| `0` | `Max digit: 0` |
@@THEORY
## Перебор цифр

~~~csharp
int max = 0;
while (n > 0)
{
    int digit = n % 10;
    if (digit > max)
    {
        max = digit;
    }
    n /= 10;
}
~~~

Начальное значение `0` корректно: цифры находятся в диапазоне `0…9`, и
максимум не может быть меньше нуля.

## Порядок

Цифры просматриваются справа налево. Для поиска максимума порядок не важен.

## Число 0

Цикл не выполнится, `max` останется `0` — это правильный ответ.

## Сравнение с суммой

| Задача | Начальное значение | Операция |
| --- | --- | --- |
| сумма цифр | `0` | `sum += digit` |
| максимум цифр | `0` | `if (digit > max) max = digit` |
| количество цифр | `0` | `count++` |
@@TESTS
| `9073` | `Max digit: 9\n` |
| `0` | `Max digit: 0\n` |
| `555` | `Max digit: 5\n` |
@@CASES
run_case "9073" $'Max digit: 9\n'
run_case "0" $'Max digit: 0\n'
run_case "555" $'Max digit: 5\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: найди максимальную цифру и выведи Max digit: <цифра>
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

        int max = 0;
        while (n > 0)
        {
            int digit = n % 10;
            if (digit > max)
            {
                max = digit;
            }
            n /= 10;
        }

        Console.WriteLine($"Max digit: {max}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // Цифры лежат в 0…9, поэтому 0 — безопасное начальное значение.
        int max = 0;
        while (n > 0)
        {
            int digit = n % 10;
            if (digit > max)
            {
                max = digit;
            }
            n /= 10;
        }

        Console.WriteLine($"Max digit: {max}");
    }
}
@@END

@@TASK
section: 04_loops
dir: 04_reverse_number
num: 4_4
title: CS_04_04. Разворот числа
topics: `long`, `while`, `% 10`, переполнение
input: Целое число
@@DESC
Разверни число задом наперёд и выведи результат:

~~~text
1000000009 → 9000000001
~~~

Ведущие нули после разворота не печатаются: `120 → 21`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1234` | `4321` |
| `120` | `21` |
| `1000000009` | `9000000001` |
@@THEORY
## Алгоритм

~~~csharp
long reversed = 0;
while (n > 0)
{
    reversed = reversed * 10 + n % 10;
    n /= 10;
}
~~~

На каждом шаге добавляем последнюю цифру справа.

## Почему long

`1000000009` после разворота даёт `9000000001`, а это больше `int.MaxValue`
(около 2,1 млрд). Если использовать `int`, произойдёт переполнение и ответ
будет неверным. `long` хранит до ~9·10¹⁸.

## Трассировка

| Шаг | n | digit | reversed |
| --- | --- | --- | --- |
| 1 | 1234 | 4 | 4 |
| 2 | 123 | 3 | 43 |
| 3 | 12 | 2 | 432 |
| 4 | 1 | 1 | 4321 |

## Ведущие нули

`120` разворачивается в `021`, но как число это `21`. Так и должно быть.
@@TESTS
| `1234` | `4321\n` |
| `120` | `21\n` |
| `1000000009` | `9000000001\n` |
@@CASES
run_case "1234" $'4321\n'
run_case "120" $'21\n'
run_case "1000000009" $'9000000001\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine());

        // TODO: разверни число и выведи результат
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine());

        long reversed = 0;
        while (n > 0)
        {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        Console.WriteLine(reversed);
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        long n = long.Parse(Console.ReadLine());

        // long нужен, потому что развёрнутое число может не влезть в int.
        long reversed = 0;
        while (n > 0)
        {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        Console.WriteLine(reversed);
    }
}
@@END

@@TASK
section: 04_loops
dir: 05_fizzbuzz
num: 4_5
title: CS_04_05. FizzBuzz
topics: `for`, `if/else`, `%`
input: Целое число `n`
@@DESC
Выведи числа от `1` до `n`, заменяя:

- кратные `3` — на `Fizz`;
- кратные `5` — на `Buzz`;
- кратные и `3`, и `5` — на `FizzBuzz`.

Каждое значение — на отдельной строке.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5` | `1`<br>`2`<br>`Fizz`<br>`4`<br>`Buzz` |
| `15` | `…`<br>`14`<br>`FizzBuzz` |
@@THEORY
## Порядок проверок

Сначала проверяем кратность `15` (или одновременно `3` и `5`), потом `3`,
потом `5`:

~~~csharp
for (int i = 1; i <= n; ++i)
{
    if (i % 15 == 0)
    {
        Console.WriteLine("FizzBuzz");
    }
    else if (i % 3 == 0)
    {
        Console.WriteLine("Fizz");
    }
    else if (i % 5 == 0)
    {
        Console.WriteLine("Buzz");
    }
    else
    {
        Console.WriteLine(i);
    }
}
~~~

Если проверить `3` раньше `15`, число `15` напечатает `Fizz`, а не `FizzBuzz`.

## Почему 15

`15` — наименьшее общее кратное `3` и `5`. Проверка `i % 15 == 0`
эквивалентна `i % 3 == 0 && i % 5 == 0`.

## Вывод числа

`Console.WriteLine(i)` автоматически вызывает `ToString`.
@@TESTS
| `5` | `1\n2\nFizz\n4\nBuzz\n` |
| `15` | `1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n` |
@@CASES
run_case "5" $'1\n2\nFizz\n4\nBuzz\n'
run_case "15" $'1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: выведи FizzBuzz от 1 до n
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        for (int i = 1; i <= n; ++i)
        {
            if (i % 15 == 0)
            {
                Console.WriteLine("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine("Fizz");
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine("Buzz");
            }
            else
            {
                Console.WriteLine(i);
            }
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

        for (int i = 1; i <= n; ++i)
        {
            // 15 проверяем первым: иначе Fizz перехватит FizzBuzz.
            if (i % 15 == 0)
            {
                Console.WriteLine("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine("Fizz");
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine("Buzz");
            }
            else
            {
                Console.WriteLine(i);
            }
        }
    }
}
@@END

@@TASK
section: 04_loops
dir: 06_unpaired_number
num: 4_6
title: CS_04_06. Непарное число
topics: XOR `^`, побитовые операции, циклы
input: `n` (нечётное), затем `n` целых чисел
@@DESC
Каждое число встречается дважды, кроме одного. Найди это число.

~~~text
5
2 3 2 1 3
→ 1
~~~

Выведи:

~~~text
Unique: 1
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`2 3 2 1 3` | `Unique: 1` |
| `3`<br>`7 7 9` | `Unique: 9` |
@@THEORY
## Свойства XOR

| Выражение | Результат |
| --- | --- |
| `a ^ a` | `0` |
| `a ^ 0` | `a` |
| `a ^ b ^ a` | `b` |

XOR коммутативен и ассоциативен, поэтому порядок чисел не важен.

## Решение

~~~csharp
int result = 0;
for (int i = 0; i < n; ++i)
{
    result ^= int.Parse(parts[i]);
}
~~~

Все пары взаимно уничтожатся, останется непарное число.

## Почему не словарь

Можно считать частоты в `Dictionary<int, int>`, но XOR решает задачу за
`O(1)` дополнительной памяти. Это классический приём.

## Ограничение

Метод работает, если каждое число, кроме одного, встречается ровно дважды.
При трёх повторениях нужен другой подход.
@@TESTS
| `5\n2 3 2 1 3` | `Unique: 1\n` |
| `3\n7 7 9` | `Unique: 9\n` |
| `1\n42` | `Unique: 42\n` |
@@CASES
run_case $'5\n2 3 2 1 3' $'Unique: 1\n'
run_case $'3\n7 7 9' $'Unique: 9\n'
run_case $'1\n42' $'Unique: 42\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: найди число без пары с помощью XOR
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
        string[] parts = Console.ReadLine().Split(' ');

        int result = 0;
        for (int i = 0; i < n; ++i)
        {
            result ^= int.Parse(parts[i]);
        }

        Console.WriteLine($"Unique: {result}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');

        // Пары одинаковых чисел дают 0, поэтому остаётся только непарное.
        int result = 0;
        for (int i = 0; i < n; ++i)
        {
            result ^= int.Parse(parts[i]);
        }

        Console.WriteLine($"Unique: {result}");
    }
}
@@END
