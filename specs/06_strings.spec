@@TASK
section: 06_strings
dir: 01_string_length
num: 6_1
title: CS_06_01. Длина строки
topics: `string.Length`, `Console.ReadLine`
input: Одна строка
@@DESC
Выведи длину строки:

~~~text
Length: 5
~~~

Пустая строка имеет длину `0`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello` | `Length: 5` |
| `C#` | `Length: 2` |
@@THEORY
## Строка в C#

`string` — неизменяемая последовательность символов `char`. Свойство
`Length` возвращает количество `char`.

~~~csharp
string line = Console.ReadLine();
Console.WriteLine($"Length: {line.Length}");
~~~

## Чтение строки

`Console.ReadLine()` читает всё до перевода строки и возвращает `string`
без символа `\n`.

Если ввод закончился, метод возвращает `null`. В задачах ввод всегда
содержит строку.

## `Length` — это не байты

`char` в C# — единица UTF-16. Для латиницы один символ — один `char`,
для кириллицы тоже. Но некоторые эмодзи занимают два `char`, поэтому
`Length` может быть больше числа видимых символов.

## Пустая строка

`"".Length` равно `0`. Это не `null`: у пустой строки можно вызывать
методы, у `null` — нельзя.
@@TESTS
| `hello` | `Length: 5\n` |
| `C#` | `Length: 2\n` |
| `` (пустая строка) | `Length: 0\n` |
@@CASES
run_case "hello" $'Length: 5\n'
run_case "C#" $'Length: 2\n'
run_case "" $'Length: 0\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: выведи длину строки в формате Length: N
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
        Console.WriteLine($"Length: {line.Length}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Length — количество char в строке (UTF-16).
        Console.WriteLine($"Length: {line.Length}");
    }
}
@@END

@@TASK
section: 06_strings
dir: 02_count_letters_digits
num: 6_2
title: CS_06_02. Буквы и цифры
topics: `foreach` по строке, `char.IsLetter`, `char.IsDigit`
input: Одна строка
@@DESC
Посчитай в строке количество букв и цифр:

~~~text
Letters: 5
Digits: 2
~~~

Остальные символы (пробелы, знаки) не считаются.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `abc12` | `Letters: 3`<br>`Digits: 2` |
| `Hi, 2025!` | `Letters: 2`<br>`Digits: 4` |
@@THEORY
## Перебор символов

Строку можно перебрать `foreach`, получая `char`:

~~~csharp
foreach (char c in line)
{
    // ...
}
~~~

## Классификация символов

~~~csharp
if (char.IsLetter(c)) letters++;
if (char.IsDigit(c)) digits++;
~~~

`char.IsLetter` учитывает буквы всех алфавитов, включая кириллицу.
`char.IsDigit` — десятичные цифры `0`–`9`.

## Альтернатива

Символ можно сравнить с диапазоном:

~~~csharp
if (c >= 'a' && c <= 'z') { }
~~~

Но это не сработает для заглавных букв и других алфавитов.
`char.IsLetter` надёжнее.

## Счётчики

Оба счётчика начинаются с нуля и увеличиваются за один проход — `O(n)`.
@@TESTS
| `abc12` | `Letters: 3\nDigits: 2\n` |
| `Hi, 2025!` | `Letters: 2\nDigits: 4\n` |
| `!!!` | `Letters: 0\nDigits: 0\n` |
@@CASES
run_case "abc12" $'Letters: 3\nDigits: 2\n'
run_case "Hi, 2025!" $'Letters: 2\nDigits: 4\n'
run_case "!!!" $'Letters: 0\nDigits: 0\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: посчитай буквы и цифры и выведи два числа
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

        int letters = 0;
        int digits = 0;
        foreach (char c in line)
        {
            if (char.IsLetter(c)) letters++;
            if (char.IsDigit(c)) digits++;
        }

        Console.WriteLine($"Letters: {letters}");
        Console.WriteLine($"Digits: {digits}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        int letters = 0;
        int digits = 0;
        // foreach по string даёт char — один символ UTF-16.
        foreach (char c in line)
        {
            if (char.IsLetter(c)) letters++;
            if (char.IsDigit(c)) digits++;
        }

        Console.WriteLine($"Letters: {letters}");
        Console.WriteLine($"Digits: {digits}");
    }
}
@@END

@@TASK
section: 06_strings
dir: 03_to_upper_lower
num: 6_3
title: CS_06_03. Верхний и нижний регистр
topics: `ToUpperInvariant`, `ToLowerInvariant`
input: Одна строка
@@DESC
Выведи строку в верхнем и нижнем регистре:

~~~text
UPPER: HELLO
lower: hello
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `Hello World` | `UPPER: HELLO WORLD`<br>`lower: hello world` |
| `C#` | `UPPER: C#`<br>`lower: c#` |
@@THEORY
## Смена регистра

~~~csharp
string upper = line.ToUpperInvariant();
string lower = line.ToLowerInvariant();
~~~

Методы возвращают **новую** строку: `string` неизменяем.

## Почему Invariant

`ToUpper()` и `ToLower()` зависят от текущей культуры. В турецкой локали
`i` превращается в `İ`, и тесты могут не совпасть. `Invariant` использует
нейтральные правила и даёт одинаковый результат на любой машине.

## Цифры и знаки

Регистр меняется только у букв. `#`, пробелы, цифры остаются как были.

## Вывод

~~~csharp
Console.WriteLine($"UPPER: {upper}");
Console.WriteLine($"lower: {lower}");
~~~
@@TESTS
| `Hello World` | `UPPER: HELLO WORLD\nlower: hello world\n` |
| `C#` | `UPPER: C#\nlower: c#\n` |
| `abc` | `UPPER: ABC\nlower: abc\n` |
@@CASES
run_case "Hello World" $'UPPER: HELLO WORLD\nlower: hello world\n'
run_case "C#" $'UPPER: C#\nlower: c#\n'
run_case "abc" $'UPPER: ABC\nlower: abc\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: выведи строку в верхнем и нижнем регистре
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
        Console.WriteLine($"UPPER: {line.ToUpperInvariant()}");
        Console.WriteLine($"lower: {line.ToLowerInvariant()}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Invariant не зависит от локали машины.
        Console.WriteLine($"UPPER: {line.ToUpperInvariant()}");
        Console.WriteLine($"lower: {line.ToLowerInvariant()}");
    }
}
@@END

@@TASK
section: 06_strings
dir: 04_count_words
num: 6_4
title: CS_06_04. Количество слов
topics: `Split`, `StringSplitOptions.RemoveEmptyEntries`
input: Одна строка со словами
@@DESC
Посчитай количество слов, разделённых пробелами:

~~~text
Words: 3
~~~

Несколько пробелов подряд считаются одним разделителем.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello world foo` | `Words: 3` |
| `  one   two  ` | `Words: 2` |
@@THEORY
## Split

~~~csharp
string[] words = line.Split(' ');
~~~

`Split` режет строку по разделителю. Пустые куски между двумя пробелами
попадут в массив как `""`.

## Убрать пустые куски

~~~csharp
string[] words = line.Split(
    new char[] { ' ', '\t' },
    StringSplitOptions.RemoveEmptyEntries);
~~~

Флаг `RemoveEmptyEntries` выбрасывает пустые элементы. Тогда
`"  one   two  "` даёт массив из двух слов.

## Количество

После `Split` число слов — это `words.Length`.

## Крайние случаи

Строка из одних пробелов даёт пустой массив, `Length` равно `0`.
Пустая строка — тоже `0`.
@@TESTS
| `hello world foo` | `Words: 3\n` |
| `  one   two  ` | `Words: 2\n` |
| `single` | `Words: 1\n` |
| `   ` | `Words: 0\n` |
@@CASES
run_case "hello world foo" $'Words: 3\n'
run_case "  one   two  " $'Words: 2\n'
run_case "single" $'Words: 1\n'
run_case "   " $'Words: 0\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: посчитай слова и выведи Words: N
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
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // RemoveEmptyEntries убирает куски между соседними пробелами.
        string[] words = line.Split(
            new char[] { ' ', '\t' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
@@END

@@TASK
section: 06_strings
dir: 05_reverse_string
num: 6_5
title: CS_06_05. Разворот строки
topics: `char[]`, `Array.Reverse`, `new string`
input: Одна строка
@@DESC
Выведи строку в обратном порядке:

~~~text
olleh
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello` | `olleh` |
| `abc def` | `fed cba` |
@@THEORY
## Строка → массив символов

~~~csharp
char[] chars = line.ToCharArray();
Array.Reverse(chars);
string reversed = new string(chars);
~~~

`Array.Reverse` меняет порядок элементов массива на месте.
`new string(chars)` собирает строку обратно.

## Почему не `line.Reverse()`

`Enumerable.Reverse()` из LINQ возвращает `IEnumerable<char>`, а не строку.
Пришлось бы вызывать `string.Concat` или `new string(...)`. Работа с
массивом нагляднее и не требует `using System.Linq`.

## Один проход без Reverse

~~~csharp
char[] result = new char[line.Length];
for (int i = 0; i < line.Length; ++i)
{
    result[i] = line[line.Length - 1 - i];
}
~~~

## Индексация

`line[i]` — символ по индексу, нумерация с нуля. Обращение за границы
бросает `IndexOutOfRangeException`.
@@TESTS
| `hello` | `olleh\n` |
| `abc def` | `fed cba\n` |
| `a` | `a\n` |
@@CASES
run_case "hello" $'olleh\n'
run_case "abc def" $'fed cba\n'
run_case "a" $'a\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: разверни строку и выведи результат
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
        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        Console.WriteLine(new string(chars));
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // Reverse работает с массивом, поэтому строка копируется в char[].
        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        Console.WriteLine(new string(chars));
    }
}
@@END

@@TASK
section: 06_strings
dir: 06_palindrome
num: 6_6
title: CS_06_06. Палиндром
topics: `char[]`, `Array.Reverse`, сравнение строк
input: Одна строка
@@DESC
Проверь, читается ли строка одинаково в обе стороны:

~~~text
True
~~~

Выведи `True` или `False`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `level` | `True` |
| `hello` | `False` |
| `a` | `True` |
@@THEORY
## Идея

Палиндром — строка, которая совпадает со своим разворотом.

~~~csharp
char[] chars = line.ToCharArray();
Array.Reverse(chars);
string reversed = new string(chars);
Console.WriteLine(line == reversed);
~~~

## Сравнение строк

В C# `==` для `string` сравнивает **содержимое**, а не ссылки. Это
отличается от Java, где `==` сравнивает ссылки.

## Логическое значение

`line == reversed` имеет тип `bool`. `Console.WriteLine` печатает его
как `True` или `False` — с заглавной буквы.

## Без копирования

Можно идти с двух концов:

~~~csharp
int i = 0;
int j = line.Length - 1;
while (i < j && line[i] == line[j])
{
    i++;
    j--;
}
bool ok = i >= j;
~~~
@@TESTS
| `level` | `True\n` |
| `hello` | `False\n` |
| `a` | `True\n` |
| `abba` | `True\n` |
@@CASES
run_case "level" $'True\n'
run_case "hello" $'False\n'
run_case "a" $'True\n'
run_case "abba" $'True\n'
@@MAIN
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        // TODO: выведи True или False
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
        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        string reversed = new string(chars);
        Console.WriteLine(line == reversed);
    }
}
@@COMMENTED
using System;

class Program
{
    static void Main()
    {
        string line = Console.ReadLine();

        char[] chars = line.ToCharArray();
        Array.Reverse(chars);
        string reversed = new string(chars);

        // == у string сравнивает содержимое.
        Console.WriteLine(line == reversed);
    }
}
@@END

@@TASK
section: 06_strings
dir: 07_caesar_cipher
num: 6_7
title: CS_06_07. Шифр Цезаря
topics: `char`, `%`, `ToCharArray`
input: Сдвиг `k`, затем строка
@@DESC
Зашифруй строку сдвигом латинских букв на `k` позиций. Регистр
сохраняется, остальные символы не меняются:

~~~text
3
abc xyz
→ def abc
~~~

Буквы зациклены: после `z` идёт `a`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`abc xyz` | `def abc` |
| `1`<br>`Hello, World!` | `Ifmmp, Xpsme!` |
| `0`<br>`No change` | `No change` |
@@THEORY
## Сдвиг буквы

Код символа `char` можно использовать в арифметике:

~~~csharp
char c = 'a';
int shifted = 'a' + (c - 'a' + k) % 26;
char result = (char)shifted;
~~~

`c - 'a'` — номер буквы от `0` до `25`. Прибавляем `k`, берём остаток
по модулю `26`, затем возвращаемся к коду буквы.

## Два диапазона

Заглавные и строчные буквы лежат в разных диапазонах, поэтому их
обрабатывают отдельно:

~~~csharp
if (c >= 'a' && c <= 'z') { }
else if (c >= 'A' && c <= 'Z') { }
~~~

## Нормализация сдвига

~~~csharp
k = ((k % 26) + 26) % 26;
~~~

Двойной остаток делает `k` неотрицательным даже для отрицательного
ввода.

## Сборка результата

`ToCharArray()` даёт изменяемый массив, `new string(chars)` собирает
строку обратно.
@@TESTS
| `3\nabc xyz` | `def abc\n` |
| `1\nHello, World!` | `Ifmmp, Xpsme!\n` |
| `0\nNo change` | `No change\n` |
| `25\nab` | `za\n` |
@@CASES
run_case $'3\nabc xyz' $'def abc\n'
run_case $'1\nHello, World!' $'Ifmmp, Xpsme!\n'
run_case $'0\nNo change' $'No change\n'
run_case $'25\nab' $'za\n'
@@MAIN
using System;

class Program
{
    static string Shift(string text, int k)
    {
        // TODO: верни зашифрованную строку
        return text;
    }

    static void Main()
    {
        int k = int.Parse(Console.ReadLine());
        string line = Console.ReadLine();

        // TODO: выведи результат Shift(line, k)
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Program
{
    static string Shift(string text, int k)
    {
        k = ((k % 26) + 26) % 26;
        char[] chars = text.ToCharArray();
        for (int i = 0; i < chars.Length; ++i)
        {
            char c = chars[i];
            if (c >= 'a' && c <= 'z')
            {
                chars[i] = (char)('a' + (c - 'a' + k) % 26);
            }
            else if (c >= 'A' && c <= 'Z')
            {
                chars[i] = (char)('A' + (c - 'A' + k) % 26);
            }
        }
        return new string(chars);
    }

    static void Main()
    {
        int k = int.Parse(Console.ReadLine());
        string line = Console.ReadLine();
        Console.WriteLine(Shift(line, k));
    }
}
@@COMMENTED
using System;

class Program
{
    static string Shift(string text, int k)
    {
        // Приводим сдвиг к диапазону 0..25.
        k = ((k % 26) + 26) % 26;
        char[] chars = text.ToCharArray();
        for (int i = 0; i < chars.Length; ++i)
        {
            char c = chars[i];
            if (c >= 'a' && c <= 'z')
            {
                // Сдвигаем внутри строчных букв.
                chars[i] = (char)('a' + (c - 'a' + k) % 26);
            }
            else if (c >= 'A' && c <= 'Z')
            {
                // Заглавные обрабатываются отдельным диапазоном.
                chars[i] = (char)('A' + (c - 'A' + k) % 26);
            }
        }
        return new string(chars);
    }

    static void Main()
    {
        int k = int.Parse(Console.ReadLine());
        string line = Console.ReadLine();
        Console.WriteLine(Shift(line, k));
    }
}
@@END
