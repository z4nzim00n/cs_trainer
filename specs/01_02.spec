@@TASK
section: 01_basics
dir: 01_hello_world
num: 1_1
title: CS_01_01. Первая программа
topics: `using System`, `class Program`, `static void Main`, `Console.WriteLine`
input: Не требуются
@@DESC
Напиши программу, которая выводит строку:

~~~text
Hello, C#!
~~~

Каждая программа на C# состоит из классов. Точка входа — статический метод
`Main`. Для консольного вывода используется `Console.WriteLine`.

~~~csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, C#!");
    }
}
~~~

`WriteLine` печатает значение и добавляет перевод строки.
@@EXAMPLES
| *(нет ввода)* | `Hello, C#!` |
@@THEORY
## Пространства имён

~~~csharp
using System;
~~~

`Console` объявлен в пространстве имён `System`. Без `using System` придётся
писать полное имя `System.Console`.

## Класс и точка входа

~~~csharp
class Program
{
    static void Main()
    {
    }
}
~~~

`Main` — статический метод, с которого начинается выполнение. Компилятор
ищет его среди классов программы. Имя класса `Program` не обязательно, но
так принято.

## Вывод

~~~csharp
Console.WriteLine("Hello, C#!"); // с переводом строки
Console.Write("Hello");          // без перевода строки
~~~

| Метод | Перевод строки |
| --- | --- |
| `Console.Write` | нет |
| `Console.WriteLine` | да |

На Windows `WriteLine` выводит `\r\n`, на Linux/macOS — `\n`. Тесты
нормализуют `\r`, поэтому формат одинаковый на всех платформах.

## Частые ошибки

| Ошибка | Сообщение компилятора |
| --- | --- |
| Нет `using System` | `The name 'Console' does not exist` |
| `Main` не статический | `Main must be static` |
| Нет класса | `Program does not contain a static 'Main' method` |
| Забыта `;` | `; expected` |
@@TESTS
| *(нет ввода)* | `Hello, C#!\n` |
@@CASES
run_case_devnull $'Hello, C#!\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        // TODO: выведи строку Hello, C#! с переводом строки
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, C#!");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        // WriteLine печатает строку и добавляет перевод строки.
        Console.WriteLine("Hello, C#!");
    }
}
@@END

@@TASK
section: 01_basics
dir: 02_fix_using
num: 1_2
title: CS_01_02. Исправь using
topics: `using System`, ошибки компиляции
input: Не требуются
@@DESC
В файле `Program.cs` есть ошибка: пропущена строка `using System;`. Из-за
этого компилятор не знает имя `Console`.

Добавь нужный `using`, чтобы программа собралась и вывела:

~~~text
Fixed!
~~~
@@EXAMPLES
| *(нет ввода)* | `Fixed!` |
@@THEORY
## Что такое using

`using System;` подключает пространство имён `System`, в котором объявлены
`Console`, `String`, `Math` и другие базовые типы.

Без этой строки каждое имя нужно писать полностью:

~~~csharp
System.Console.WriteLine("Fixed!");
~~~

## Сообщение компилятора

~~~text
error CS0103: The name 'Console' does not exist in the current context
~~~

Это не ошибка логики, а отсутствующий импорт. Такое сообщение часто
означает, что забыт `using` или подключена не та библиотека.

## Порядок исправления

1. Прочитай первую ошибку компилятора.
2. Найди имя, которое он не узнаёт.
3. Проверь, подключено ли его пространство имён.
4. Пересобери программу.
@@TESTS
| *(нет ввода)* | `Fixed!\n` |
@@CASES
run_case_devnull $'Fixed!\n'
@@MAIN
// TODO: добавь using System;
class Program
{
    static void Main()
    {
        Console.WriteLine("Fixed!");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Fixed!");
    }
}
@@COMMENTED
// using подключает пространство имён System,
// где объявлен класс Console.
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Fixed!");
    }
}
@@END

@@TASK
section: 01_basics
dir: 03_fix_semicolon
num: 1_3
title: CS_01_03. Исправь точку с запятой
topics: инструкции, `;`, ошибки компиляции
input: Не требуются
@@DESC
В программе пропущена точка с запятой после объявления переменной.
Исправь код, чтобы он вывел:

~~~text
Ready
~~~
@@EXAMPLES
| *(нет ввода)* | `Ready` |
@@THEORY
## Точка с запятой

Каждая инструкция в C# заканчивается символом `;`:

~~~csharp
int x = 10;
Console.WriteLine(x);
~~~

После блока `{ ... }` точка с запятой не нужна. После объявления класса,
метода и условия — тоже.

## Сообщение компилятора

~~~text
error CS1002: ; expected
~~~

Компилятор сообщает строку, где заметил проблему, но реальная причина
может быть на строку выше. Если `; expected` указывает на `Console`, проверь
предыдущую инструкцию.

## Типичные места

| Код | Нужна `;` |
| --- | --- |
| `int x = 1` | да |
| `Console.WriteLine(x)` | да |
| `class Program { }` | нет |
| `if (x > 0) { }` | нет |
@@TESTS
| *(нет ввода)* | `Ready\n` |
@@CASES
run_case_devnull $'Ready\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        int version = 1
        Console.WriteLine("Ready");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        int version = 1;
        Console.WriteLine("Ready");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        // Каждая инструкция завершается точкой с запятой.
        int version = 1;
        Console.WriteLine("Ready");
    }
}
@@END

@@TASK
section: 01_basics
dir: 04_variables_output
num: 1_4
title: CS_01_04. Переменные
topics: переменные, `int`, `string`, интерполяция строк
input: Не требуются
@@DESC
Создай две переменные:

- `language` со значением `C#`;
- `year` со значением `2000`.

Выведи:

~~~text
Language: C#
Year: 2000
~~~
@@EXAMPLES
| *(нет ввода)* | `Language: C#`<br>`Year: 2000` |
@@THEORY
## Объявление переменных

~~~csharp
string language = "C#";
int year = 2000;
~~~

Тип указывается перед именем. `string` хранит текст, `int` — целое число.

## Вывод нескольких значений

~~~csharp
Console.WriteLine("Language: " + language);
Console.WriteLine("Year: " + year);
~~~

Или интерполяция:

~~~csharp
Console.WriteLine($"Language: {language}");
Console.WriteLine($"Year: {year}");
~~~

Символ `$` перед строкой включает подстановку выражений в `{ ... }`.

## Типы

| Тип | Пример | Назначение |
| --- | --- | --- |
| `int` | `42` | целые числа |
| `long` | `9000000000L` | большие целые |
| `double` | `3.14` | дробные числа |
| `bool` | `true` | логический |
| `string` | `"text"` | строка |
| `char` | `'A'` | один символ |

`var` позволяет вывести тип:

~~~csharp
var language = "C#"; // string
var year = 2000;     // int
~~~
@@TESTS
| *(нет ввода)* | `Language: C#\nYear: 2000\n` |
@@CASES
run_case_devnull $'Language: C#\nYear: 2000\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string language = "C#";
        int year = 2000;

        // TODO: выведи две строки: Language: C# и Year: 2000
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string language = "C#";
        int year = 2000;

        Console.WriteLine("Language: " + language);
        Console.WriteLine("Year: " + year);
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string language = "C#";
        int year = 2000;

        // Интерполяция подставляет значения переменных в строку.
        Console.WriteLine($"Language: {language}");
        Console.WriteLine($"Year: {year}");
    }
}
@@END

@@TASK
section: 01_basics
dir: 05_swap_two_numbers
num: 1_5
title: CS_01_05. Обмен значений
topics: `int`, временная переменная, `Console.ReadLine`, `Split`
input: Два целых числа через пробел
@@DESC
Считай два целых числа и выведи их в обратном порядке через пробел:

~~~text
<b> <a>
~~~

Например, для `3 5` вывод должен быть `5 3`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 5` | `5 3` |
| `-1 10` | `10 -1` |
@@THEORY
## Чтение строки и разбиение

~~~csharp
string line = Console.ReadLine();
string[] parts = line.Split(' ');
int a = int.Parse(parts[0]);
int b = int.Parse(parts[1]);
~~~

`ReadLine` возвращает строку целиком. `Split(' ')` делит её по пробелам.
`int.Parse` превращает текст в число.

## Обмен значений

~~~csharp
int temp = a;
a = b;
b = temp;
~~~

Без временной переменной первое значение потеряется.

## Вывод

~~~csharp
Console.WriteLine(a + " " + b);
~~~

`+` склеивает строку и числа. Порядок важен: `" " + a` тоже сработает,
но `a + b + " "` сначала сложит числа.

## Крайние случаи

`int.Parse` не прощает лишних символов. Если строка пустая или содержит
буквы, программа завершится исключением `FormatException`. В задачах
ввод корректный.
@@TESTS
| `3 5` | `5 3\n` |
| `-1 10` | `10 -1\n` |
@@CASES
run_case "3 5" $'5 3\n'
run_case "-1 10" $'10 -1\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // TODO: поменяй значения местами и выведи их через пробел
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

        int temp = a;
        a = b;
        b = temp;

        Console.WriteLine(a + " " + b);
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

        // Временная переменная сохраняет a, пока мы записываем в неё b.
        int temp = a;
        a = b;
        b = temp;

        Console.WriteLine(a + " " + b);
    }
}
@@END
