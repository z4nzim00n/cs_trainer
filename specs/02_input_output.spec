@@TASK
section: 02_input_output
dir: 01_echo_number
num: 2_1
title: CS_02_01. Эхо числа
topics: `Console.ReadLine`, `int.Parse`, интерполяция
input: Одно целое число
@@DESC
Считай целое число и выведи его в формате:

~~~text
Number: <число>
~~~

Например, для `42` вывод `Number: 42`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `42` | `Number: 42` |
| `-7` | `Number: -7` |
@@THEORY
## Чтение числа

~~~csharp
string line = Console.ReadLine();
int number = int.Parse(line);
~~~

`ReadLine` возвращает строку. `int.Parse` разбирает её как целое число.

## Вывод

~~~csharp
Console.WriteLine($"Number: {number}");
~~~

Интерполяция `$"..."` подставляет значение в фигурные скобки.

## Что если ввести не число

`int.Parse("abc")` бросает `FormatException`. Позже, в разделе про
исключения, мы научимся обрабатывать такие случаи через `int.TryParse`.
@@TESTS
| `42` | `Number: 42\n` |
| `-7` | `Number: -7\n` |
@@CASES
run_case "42" $'Number: 42\n'
run_case "-7" $'Number: -7\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: преобразуй строку в число и выведи Number: <число>
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        int number = int.Parse(line);

        Console.WriteLine($"Number: {number}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Parse превращает текст в число.
        int number = int.Parse(line);

        Console.WriteLine($"Number: {number}");
    }
}
@@END

@@TASK
section: 02_input_output
dir: 02_sum_two_numbers
num: 2_2
title: CS_02_02. Сумма двух чисел
topics: `Split`, `int.Parse`, арифметика
input: Два целых числа через пробел
@@DESC
Считай два целых числа и выведи их сумму:

~~~text
Sum: <сумма>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2 3` | `Sum: 5` |
| `-4 4` | `Sum: 0` |
@@THEORY
## Разбор строки

~~~csharp
string[] parts = Console.ReadLine().Split(' ');
int a = int.Parse(parts[0]);
int b = int.Parse(parts[1]);
~~~

Массив `parts` содержит части строки. Индексы начинаются с нуля.

## Сложение

~~~csharp
int sum = a + b;
Console.WriteLine($"Sum: {sum}");
~~~

## Переполнение

`int` хранит примерно от -2 млрд до 2 млрд. Сумма двух больших чисел может
переполниться. Для таких случаев есть `long`:

~~~csharp
long sum = (long)a + b;
~~~

В задаче числа небольшие, но помнить об ограничении полезно.
@@TESTS
| `2 3` | `Sum: 5\n` |
| `-4 4` | `Sum: 0\n` |
| `100 200` | `Sum: 300\n` |
@@CASES
run_case "2 3" $'Sum: 5\n'
run_case "-4 4" $'Sum: 0\n'
run_case "100 200" $'Sum: 300\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // TODO: выведи Sum: <a + b>
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

        int sum = a + b;
        Console.WriteLine($"Sum: {sum}");
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

        // Сначала вычисляем, потом печатаем.
        int sum = a + b;
        Console.WriteLine($"Sum: {sum}");
    }
}
@@END

@@TASK
section: 02_input_output
dir: 03_read_full_line
num: 2_3
title: CS_02_03. Строка целиком
topics: `Console.ReadLine`, пробелы в строке
input: Одна строка текста
@@DESC
Считай строку целиком, включая пробелы, и выведи:

~~~text
Line: <строка>
~~~

Например, для `hello world` вывод `Line: hello world`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello world` | `Line: hello world` |
| `a  b` | `Line: a  b` |
@@THEORY
## ReadLine читает всю строку

~~~csharp
string line = Console.ReadLine();
~~~

`ReadLine` читает символы до конца строки и возвращает их вместе с пробелами.
Это отличает его от чтения по словам через `Split`.

## Вывод с префиксом

~~~csharp
Console.WriteLine("Line: " + line);
~~~

Если строка пустая, вывод будет `Line: ` — префикс и пробел останутся.

## ReadLine и конец ввода

В конце файла `ReadLine` возвращает `null`. В интерактивной консоли это
означает Ctrl+Z (Windows) или Ctrl+D (Linux/macOS). В задачах ввод всегда
содержит строку.

## Сравнение способов

| Способ | Что читает |
| --- | --- |
| `ReadLine` | всю строку |
| `ReadLine().Split(' ')` | строку, затем делит по пробелам |
| `int.Parse(ReadLine())` | строку и сразу разбирает число |
@@TESTS
| `hello world` | `Line: hello world\n` |
| `a  b` | `Line: a  b\n` |
@@CASES
run_case "hello world" $'Line: hello world\n'
run_case "a  b" $'Line: a  b\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: выведи Line: <введённая строка>
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        Console.WriteLine("Line: " + line);
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        // ReadLine сохраняет пробелы внутри строки.
        string line = Console.ReadLine();
        Console.WriteLine("Line: " + line);
    }
}
@@END

@@TASK
section: 02_input_output
dir: 04_formatted_output
num: 2_4
title: CS_02_04. Форматирование числа
topics: `double`, `CultureInfo.InvariantCulture`, формат `F2`
input: Одно дробное число
@@DESC
Считай дробное число и выведи его с двумя знаками после точки:

~~~text
Value: 3.14
~~~

Разделитель — точка, независимо от региональных настроек.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3.14159` | `Value: 3.14` |
| `2` | `Value: 2.00` |
@@THEORY
## Дробные числа

~~~csharp
double value = double.Parse(line, CultureInfo.InvariantCulture);
~~~

`double` хранит число с плавающей точкой. `CultureInfo.InvariantCulture`
заставляет парсер ожидать точку, а не запятую.

## Формат F2

~~~csharp
string text = value.ToString("F2", CultureInfo.InvariantCulture);
Console.WriteLine("Value: " + text);
~~~

`F2` означает фиксированный формат с двумя знаками после разделителя.
Без `InvariantCulture` на русской Windows получится `3,14`.

## Зачем InvariantCulture

| Культура | Вывод |
| --- | --- |
| Invariant | `3.14` |
| ru-RU | `3,14` |
| de-DE | `3,14` |

Тесты ожидают точку. Поэтому формат задаётся явно.

## Округление

`F2` округляет по правилам .NET. Например, `2.345` может дать `2.35`
или `2.34` из-за двоичного представления `double`. В задачах значения
подобраны без спорных границ.
@@TESTS
| `3.14159` | `Value: 3.14\n` |
| `2` | `Value: 2.00\n` |
| `0.5` | `Value: 0.50\n` |
@@CASES
run_case "3.14159" $'Value: 3.14\n'
run_case "2" $'Value: 2.00\n'
run_case "0.5" $'Value: 0.50\n'
@@MAIN
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        // TODO: выведи Value: <значение с двумя знаками>
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
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        string text = value.ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine("Value: " + text);
    }
}
@@COMMENTED
using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();
        double value = double.Parse(line, CultureInfo.InvariantCulture);

        // F2 — два знака после точки; InvariantCulture фиксирует точку.
        string text = value.ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine("Value: " + text);
    }
}
@@END

@@TASK
section: 02_input_output
dir: 05_mixed_input
num: 2_5
title: CS_02_05. Смешанный ввод
topics: `Split`, `int.Parse`, `string`, несколько значений
input: Возраст и имя через пробел
@@DESC
В одной строке заданы целое число и имя. Выведи:

~~~text
Age: <возраст>
Name: <имя>
~~~

Например, для `42 Bob`:

~~~text
Age: 42
Name: Bob
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `42 Bob` | `Age: 42`<br>`Name: Bob` |
| `7 Alice` | `Age: 7`<br>`Name: Alice` |
@@THEORY
## Два значения в одной строке

~~~csharp
string[] parts = Console.ReadLine().Split(' ');
int age = int.Parse(parts[0]);
string name = parts[1];
~~~

Первая часть — число, вторая — строка. `int.Parse` нужен только для числа.

## Вывод

~~~csharp
Console.WriteLine($"Age: {age}");
Console.WriteLine($"Name: {name}");
~~~

## А если имя из двух слов

`Split(' ')` разделит `Anna Maria` на три части, и `parts[1]` будет только
`Anna`. Для имён с пробелами нужен другой формат ввода или `Split` с
ограничением количества частей. В этой задаче имя состоит из одного слова.

## Проверка количества частей

В реальном коде стоит проверить `parts.Length`, прежде чем обращаться
к `parts[1]`. Иначе при неверном вводе будет `IndexOutOfRangeException`.
@@TESTS
| `42 Bob` | `Age: 42\nName: Bob\n` |
| `7 Alice` | `Age: 7\nName: Alice\n` |
@@CASES
run_case "42 Bob" $'Age: 42\nName: Bob\n'
run_case "7 Alice" $'Age: 7\nName: Alice\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int age = int.Parse(parts[0]);
        string name = parts[1];

        // TODO: выведи возраст и имя на отдельных строках
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
        int age = int.Parse(parts[0]);
        string name = parts[1];

        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"Name: {name}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');

        // parts[0] — текст числа, parts[1] — имя.
        int age = int.Parse(parts[0]);
        string name = parts[1];

        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"Name: {name}");
    }
}
@@END
