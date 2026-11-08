@@TASK
section: 09_errors
dir: 01_safe_division
num: 9_1
title: CS_09_01. Безопасное деление
topics: `try`/`catch`, `DivideByZeroException`
input: Два целых числа `a` и `b`
@@DESC
Раздели `a` на `b`. Если `b` равно нулю, не падай, а выведи ошибку:

~~~text
Result: 5
~~~

~~~text
Error: division by zero
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `10 2` | `Result: 5` |
| `7 0` | `Error: division by zero` |
@@THEORY
## Исключение при делении

Целочисленное деление на ноль бросает `DivideByZeroException`. Без
обработки программа завершится с ошибкой.

## `try` / `catch`

~~~csharp
try
{
    int result = a / b;
    Console.WriteLine($"Result: {result}");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Error: division by zero");
}
~~~

Код в `try` выполняется, пока не возникнет исключение. Управление
переходит в подходящий `catch`.

## Порядок `catch`

`catch` проверяются сверху вниз, срабатывает первый подходящий. Более
общие исключения (`Exception`) ставьте последними.

## Альтернатива без исключения

~~~csharp
if (b == 0)
{
    Console.WriteLine("Error: division by zero");
}
else
{
    Console.WriteLine($"Result: {a / b}");
}
~~~

Проверка дешевле исключения, но `try`/`catch` показывает механизм,
который нужен для непредсказуемых ошибок.

## Отрицательные числа

Деление целых в C# отбрасывает дробную часть к нулю: `-7 / 2 == -3`.
@@TESTS
| `10 2` | `Result: 5\n` |
| `7 0` | `Error: division by zero\n` |
| `-7 2` | `Result: -3\n` |
@@CASES
run_case "10 2" $'Result: 5\n'
run_case "7 0" $'Error: division by zero\n'
run_case "-7 2" $'Result: -3\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // TODO: раздели a на b, обработай деление на ноль
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

        try
        {
            int result = a / b;
            Console.WriteLine($"Result: {result}");
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Error: division by zero");
        }
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

        // Деление на ноль — исключение, его можно перехватить.
        try
        {
            int result = a / b;
            Console.WriteLine($"Result: {result}");
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Error: division by zero");
        }
    }
}
@@END

@@TASK
section: 09_errors
dir: 02_parse_int
num: 9_2
title: CS_09_02. Разбор числа
topics: `int.TryParse`, `out`, ветвление
input: Одна строка
@@DESC
Преобразуй строку в число. Если это невозможно, выведи `Invalid number`:

~~~text
Number: 42
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `42` | `Number: 42` |
| `abc` | `Invalid number` |
| `-7` | `Number: -7` |
@@THEORY
## `Parse` и `TryParse`

`int.Parse("abc")` бросает `FormatException`. `int.TryParse` вместо
исключения возвращает `bool`:

~~~csharp
if (int.TryParse(input, out int value))
{
    Console.WriteLine($"Number: {value}");
}
else
{
    Console.WriteLine("Invalid number");
}
~~~

## `out`-параметр

`TryParse` записывает результат в переменную `value`. Если разбор не
удался, там будет `0`, но полагаться на это не нужно — сначала
проверяйте `true`.

С C# 7 переменную можно объявить прямо в вызове: `out int value`.

## Что считается числом

`TryParse` принимает необязательный знак и цифры. Пробелы по краям
допускаются. Пустая строка и буквы дают `false`.

## Когда что использовать

- Ввод пользователя — `TryParse`, ошибка ожидаема.
- Данные, которые обязаны быть корректными, — `Parse`, пусть падает
  громко.
@@TESTS
| `42` | `Number: 42\n` |
| `abc` | `Invalid number\n` |
| `-7` | `Number: -7\n` |
| `` (пустая строка) | `Invalid number\n` |
@@CASES
run_case "42" $'Number: 42\n'
run_case "abc" $'Invalid number\n'
run_case "-7" $'Number: -7\n'
run_case "" $'Invalid number\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();

        // TODO: разбери число и выведи Number или Invalid number
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();
        if (int.TryParse(input, out int value))
        {
            Console.WriteLine($"Number: {value}");
        }
        else
        {
            Console.WriteLine("Invalid number");
        }
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();

        // TryParse не бросает исключение — возвращает true или false.
        if (int.TryParse(input, out int value))
        {
            Console.WriteLine($"Number: {value}");
        }
        else
        {
            Console.WriteLine("Invalid number");
        }
    }
}
@@END

@@TASK
section: 09_errors
dir: 03_custom_exception
num: 9_3
title: CS_09_03. Своё исключение
topics: `Exception`, конструктор, `throw`, `catch`
input: Возраст (целое число)
@@DESC
Опиши исключение `NegativeAgeException`. Если возраст отрицательный,
брось его и выведи сообщение:

~~~text
Age: 20
~~~

~~~text
Error: age cannot be negative
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `20` | `Age: 20` |
| `-5` | `Error: age cannot be negative` |
@@THEORY
## Свой класс исключения

~~~csharp
class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}
~~~

Наследование от `Exception` делает класс бросаемым. Конструктор передаёт
сообщение в базовый класс, его вернёт свойство `Message`.

## Бросок

~~~csharp
if (age < 0)
{
    throw new NegativeAgeException("age cannot be negative");
}
~~~

`throw` прерывает текущий метод и ищет подходящий `catch` выше по стеку.

## Перехват конкретного типа

~~~csharp
try
{
    // ...
}
catch (NegativeAgeException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}
~~~

## Зачем свои исключения

Тип исключения говорит, что именно пошло не так. Вызывающий код может
обработать `NegativeAgeException` отдельно от остальных ошибок.

## Соглашение об именах

Имена классов исключений заканчиваются на `Exception`.
@@TESTS
| `20` | `Age: 20\n` |
| `-5` | `Error: age cannot be negative\n` |
| `0` | `Age: 0\n` |
@@CASES
run_case "20" $'Age: 20\n'
run_case "-5" $'Error: age cannot be negative\n'
run_case "0" $'Age: 0\n'
@@MAIN
using System;

class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}

class Program
{
    static void Main()
    {
        int age = int.Parse(Console.ReadLine());

        // TODO: брось NegativeAgeException для возраста < 0
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}

class Program
{
    static void Main()
    {
        int age = int.Parse(Console.ReadLine());

        try
        {
            if (age < 0)
            {
                throw new NegativeAgeException("age cannot be negative");
            }
            Console.WriteLine($"Age: {age}");
        }
        catch (NegativeAgeException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
@@COMMENTED
using System;

class NegativeAgeException : Exception
{
    // base(message) сохраняет текст в свойстве Message.
    public NegativeAgeException(string message) : base(message)
    {
    }
}

class Program
{
    static void Main()
    {
        int age = int.Parse(Console.ReadLine());

        try
        {
            if (age < 0)
            {
                throw new NegativeAgeException("age cannot be negative");
            }
            Console.WriteLine($"Age: {age}");
        }
        catch (NegativeAgeException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
@@END

@@TASK
section: 09_errors
dir: 04_using_scope
num: 9_4
title: CS_09_04. `using` и `IDisposable`
topics: `IDisposable`, `using`, детерминированный порядок
input: Имя ресурса
@@DESC
Опиши класс `Resource`, который печатает `Open: имя` при создании и
`Close: имя` при освобождении. Используй `using`:

~~~text
Open: data
Use: data
Close: data
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `data` | `Open: data`<br>`Use: data`<br>`Close: data` |
| `log` | `Open: log`<br>`Use: log`<br>`Close: log` |
@@THEORY
## `IDisposable`

Интерфейс с одним методом:

~~~csharp
class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
        Console.WriteLine($"Open: {name}");
    }

    public void Dispose()
    {
        Console.WriteLine($"Close: {name}");
    }
}
~~~

## `using`

~~~csharp
using (Resource r = new Resource(name))
{
    Console.WriteLine($"Use: {name}");
}
~~~

`using` вызывает `Dispose()` при выходе из блока, даже если внутри
произошло исключение. Это аналог `try/finally`.

## Порядок вызовов

1. Конструктор — `Open`.
2. Тело блока — `Use`.
3. `Dispose` — `Close`.

Такой порядок детерминирован, поэтому его удобно проверять тестами.

## Сокращённая запись

С C# 8 можно писать `using Resource r = new Resource(name);` — `Dispose`
вызовется в конце области видимости.
@@TESTS
| `data` | `Open: data\nUse: data\nClose: data\n` |
| `log` | `Open: log\nUse: log\nClose: log\n` |
@@CASES
run_case "data" $'Open: data\nUse: data\nClose: data\n'
run_case "log" $'Open: log\nUse: log\nClose: log\n'
@@MAIN
using System;

class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
    }

    public void Dispose()
    {
        // TODO: напечатай Close: имя
    }
}

class Program
{
    static void Main()
    {
        string name = Console.ReadLine();

        // TODO: открой ресурс через using, напечатай Use: имя
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
        Console.WriteLine($"Open: {name}");
    }

    public void Dispose()
    {
        Console.WriteLine($"Close: {name}");
    }
}

class Program
{
    static void Main()
    {
        string name = Console.ReadLine();

        using (Resource r = new Resource(name))
        {
            Console.WriteLine($"Use: {name}");
        }
    }
}
@@COMMENTED
using System;

class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
        // Конструктор срабатывает при входе в using.
        Console.WriteLine($"Open: {name}");
    }

    public void Dispose()
    {
        // Dispose вызывается при выходе из блока.
        Console.WriteLine($"Close: {name}");
    }
}

class Program
{
    static void Main()
    {
        string name = Console.ReadLine();

        using (Resource r = new Resource(name))
        {
            Console.WriteLine($"Use: {name}");
        }
    }
}
@@END

@@TASK
section: 09_errors
dir: 05_index_out_of_range
num: 9_5
title: CS_09_05. Выход за границы
topics: массив, `IndexOutOfRangeException`, `try`/`catch`
input: `n`, затем `n` чисел, затем индекс
@@DESC
Выведи элемент массива по индексу. Если индекс вне диапазона,
выведи ошибку:

~~~text
Value: 3
~~~

~~~text
Error: index out of range
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5`<br>`2` | `Value: 3` |
| `5`<br>`1 2 3 4 5`<br>`10` | `Error: index out of range` |
| `3`<br>`1 2 3`<br>`-1` | `Error: index out of range` |
@@THEORY
## Границы массива

Массив из `n` элементов имеет индексы `0..n-1`. Обращение к `numbers[n]`
или `numbers[-1]` бросает `IndexOutOfRangeException`.

## Перехват

~~~csharp
try
{
    int value = numbers[index];
    Console.WriteLine($"Value: {value}");
}
catch (IndexOutOfRangeException)
{
    Console.WriteLine("Error: index out of range");
}
~~~

## Массив или список

У `List<T>` индексатор бросает `ArgumentOutOfRangeException`, а не
`IndexOutOfRangeException`. Поэтому здесь используется массив `int[]`, и
тип в `catch` совпадает.

## Проверка заранее

~~~csharp
if (index >= 0 && index < numbers.Length)
{
    // безопасно
}
~~~

Явная проверка дешевле исключения. `try`/`catch` уместен, когда индекс
приходит из ненадёжного источника и проверок много.

## Пустой массив

При `n = 0` любой индекс некорректен, включая `0`.
@@TESTS
| `5\n1 2 3 4 5\n2` | `Value: 3\n` |
| `5\n1 2 3 4 5\n10` | `Error: index out of range\n` |
| `3\n1 2 3\n-1` | `Error: index out of range\n` |
| `1\n7\n0` | `Value: 7\n` |
@@CASES
run_case $'5\n1 2 3 4 5\n2' $'Value: 3\n'
run_case $'5\n1 2 3 4 5\n10' $'Error: index out of range\n'
run_case $'3\n1 2 3\n-1' $'Error: index out of range\n'
run_case $'1\n7\n0' $'Value: 7\n'
@@MAIN
using System;

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

        int index = int.Parse(Console.ReadLine());

        // TODO: выведи numbers[index] или сообщение об ошибке
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
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int index = int.Parse(Console.ReadLine());

        try
        {
            int value = numbers[index];
            Console.WriteLine($"Value: {value}");
        }
        catch (IndexOutOfRangeException)
        {
            Console.WriteLine("Error: index out of range");
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
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int index = int.Parse(Console.ReadLine());

        // Индексатор массива проверяет границы и бросает исключение.
        try
        {
            int value = numbers[index];
            Console.WriteLine($"Value: {value}");
        }
        catch (IndexOutOfRangeException)
        {
            Console.WriteLine("Error: index out of range");
        }
    }
}
@@END
