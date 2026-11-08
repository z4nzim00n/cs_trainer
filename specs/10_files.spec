@@TASK
section: 10_files
dir: 01_read_file
num: 10_1
title: CS_10_01. Чтение файла
topics: `File.ReadAllText`, `FileNotFoundException`
input: Имя файла
@@DESC
Прочитай файл и выведи его содержимое без изменений:

~~~text
hello
world
~~~

Если файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `input.txt` (содержит `hello`) | `hello` |
| `missing.txt` | `Error: file not found` |
@@THEORY
## `System.IO`

Классы для файлов лежат в пространстве имён `System.IO`:

~~~csharp
using System.IO;
~~~

## Чтение целиком

~~~csharp
string text = File.ReadAllText(path);
Console.Write(text);
~~~

`ReadAllText` возвращает строку со всеми переводами строк. `Console.Write`
печатает её без добавления своего `\n` — содержимое останется точным.

## Файла нет

`ReadAllText` бросает `FileNotFoundException`:

~~~csharp
try
{
    string text = File.ReadAllText(path);
    Console.Write(text);
}
catch (FileNotFoundException)
{
    Console.WriteLine("Error: file not found");
}
~~~

## Путь

Относительный путь считается от текущего каталога процесса. В тестах
это папка задания.
@@TESTS
| `input.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `input.txt` (`abc`, без `\n`) | `abc` |
| `missing.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f input.txt missing.txt' EXIT
printf 'hello\nworld\n' > input.txt
run_case "input.txt" $'hello\nworld\n'
printf 'abc' > input.txt
run_case "input.txt" "abc"
run_case "missing.txt" $'Error: file not found\n'
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // TODO: прочитай файл и выведи содержимое
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        try
        {
            string text = File.ReadAllText(path);
            Console.Write(text);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Error: file not found");
        }
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // Write не добавляет перевод строки — вывод совпадает с файлом.
        try
        {
            string text = File.ReadAllText(path);
            Console.Write(text);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Error: file not found");
        }
    }
}
@@END

@@TASK
section: 10_files
dir: 02_write_file
num: 10_2
title: CS_10_02. Запись файла
topics: `File.WriteAllText`, перезапись
input: Имя файла и строка
@@DESC
Запиши строку в файл и подтверди:

~~~text
Written: output.txt
~~~

Если файл уже существовал, он перезаписывается.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `output.txt`<br>`hello` | `Written: output.txt` |
@@THEORY
## Запись целиком

~~~csharp
File.WriteAllText(path, text);
~~~

Метод создаёт файл или полностью заменяет его содержимое. Каталог
должен существовать.

## Кодировка

По умолчанию `WriteAllText` пишет UTF-8 без BOM. Для явного выбора
есть перегрузка с `Encoding`:

~~~csharp
File.WriteAllText(path, text, Encoding.UTF8);
~~~

## Перевод строки

`WriteAllText` не добавляет `\n` автоматически. Если нужен перевод
строки, добавьте его в строку:

~~~csharp
File.WriteAllText(path, text + Environment.NewLine);
~~~

## Подтверждение

~~~csharp
Console.WriteLine($"Written: {path}");
~~~

## Ошибки

Нет прав или каталога — `UnauthorizedAccessException` или
`DirectoryNotFoundException`. В задаче путь корректен.
@@TESTS
| `output.txt\nhello` | `Written: output.txt\n`, файл `hello` |
| `text.txt\nhello world` | `Written: text.txt\n`, файл `hello world` |
@@CASES
trap 'rm -f output.txt text.txt' EXIT
run_case $'output.txt\nhello' $'Written: output.txt\n'
check_file "output.txt" "hello"
run_case $'text.txt\nhello world' $'Written: text.txt\n'
check_file "text.txt" "hello world"
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = Console.ReadLine();

        // TODO: запиши text в файл и выведи Written: путь
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = Console.ReadLine();

        File.WriteAllText(path, text);
        Console.WriteLine($"Written: {path}");
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = Console.ReadLine();

        // WriteAllText создаёт файл или перезаписывает существующий.
        File.WriteAllText(path, text);
        Console.WriteLine($"Written: {path}");
    }
}
@@END

@@TASK
section: 10_files
dir: 03_copy_file
num: 10_3
title: CS_10_03. Копирование файла
topics: `File.Copy`, перезапись, `check_file`
input: Исходный файл и файл назначения
@@DESC
Скопируй файл и подтверди:

~~~text
Copied: copy.txt
~~~

Если файл назначения существует, он заменяется.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `input.txt`<br>`copy.txt` | `Copied: copy.txt` |
@@THEORY
## Копирование

~~~csharp
File.Copy(source, destination, true);
~~~

Третий аргумент `overwrite: true` разрешает заменить существующий файл.
Без него при наличии файла бросается `IOException`.

## Проверка

После копирования содержимое должно совпадать:

~~~csharp
string original = File.ReadAllText(source);
string copy = File.ReadAllText(destination);
bool same = original == copy;
~~~

## Отличие от перемещения

`File.Move` переносит файл, исходный исчезает. `File.Copy` оставляет
оба.

## Ошибки

- исходного файла нет — `FileNotFoundException`;
- нет прав на запись — `UnauthorizedAccessException`;
- destination указывает на каталог — `IOException`.
@@TESTS
| `input.txt\ncopy.txt` | `Copied: copy.txt\n`, файл `abc\n` |
| повторное копирование поверх старого | файл заменён |
@@CASES
trap 'rm -f input.txt copy.txt' EXIT
printf 'abc\n' > input.txt
run_case $'input.txt\ncopy.txt' $'Copied: copy.txt\n'
check_file "copy.txt" $'abc\n'
printf 'old\n' > copy.txt
run_case $'input.txt\ncopy.txt' $'Copied: copy.txt\n'
check_file "copy.txt" $'abc\n'
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string source = Console.ReadLine();
        string destination = Console.ReadLine();

        // TODO: скопируй файл с перезаписью и выведи Copied: путь
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string source = Console.ReadLine();
        string destination = Console.ReadLine();

        File.Copy(source, destination, true);
        Console.WriteLine($"Copied: {destination}");
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string source = Console.ReadLine();
        string destination = Console.ReadLine();

        // true разрешает перезаписать существующий файл.
        File.Copy(source, destination, true);
        Console.WriteLine($"Copied: {destination}");
    }
}
@@END

@@TASK
section: 10_files
dir: 04_sum_numbers_file
num: 10_4
title: CS_10_04. Сумма чисел из файла
topics: `ReadAllText`, `Split`, `long`
input: Имя файла с числами
@@DESC
Прочитай числа из файла и выведи их сумму:

~~~text
Sum: 15
~~~

Числа разделены пробелами и переводами строк.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `numbers.txt` (`1 2 3` / `4 5`) | `Sum: 15` |
@@THEORY
## Чтение и разбор

~~~csharp
string text = File.ReadAllText(path);
string[] parts = text.Split(
    new char[] { ' ', '\t', '\r', '\n' },
    StringSplitOptions.RemoveEmptyEntries);
~~~

`RemoveEmptyEntries` убирает пустые куски между разделителями.

## Сумма

~~~csharp
long sum = 0;
foreach (string part in parts)
{
    sum += int.Parse(part);
}
~~~

`long` защищает от переполнения при большом количестве чисел.

## Альтернатива по строкам

~~~csharp
foreach (string line in File.ReadAllLines(path))
{
    foreach (string part in line.Split(' '))
    {
        // ...
    }
}
~~~

## Файла нет

`ReadAllText` бросит `FileNotFoundException`. Обработайте её, если файл
может отсутствовать.
@@TESTS
| `numbers.txt` (`1 2 3\n4 5\n`) | `Sum: 15\n` |
| `numbers.txt` (`-1 10`) | `Sum: 9\n` |
| `numbers.txt` (`42`) | `Sum: 42\n` |
@@CASES
trap 'rm -f numbers.txt' EXIT
printf '1 2 3\n4 5\n' > numbers.txt
run_case "numbers.txt" $'Sum: 15\n'
printf -- '-1 10' > numbers.txt
run_case "numbers.txt" $'Sum: 9\n'
printf '42' > numbers.txt
run_case "numbers.txt" $'Sum: 42\n'
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // TODO: прочитай числа, сложи и выведи Sum
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);
        string[] parts = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);

        long sum = 0;
        foreach (string part in parts)
        {
            sum += int.Parse(part);
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);

        // Один Split по всем видам пробелов.
        string[] parts = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);

        long sum = 0;
        foreach (string part in parts)
        {
            sum += int.Parse(part);
        }

        Console.WriteLine($"Sum: {sum}");
    }
}
@@END

@@TASK
section: 10_files
dir: 05_count_words_file
num: 10_5
title: CS_10_05. Слова в файле
topics: `ReadAllText`, `Split`, подсчёт
input: Имя файла
@@DESC
Посчитай количество слов в файле:

~~~text
Words: 3
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `text.txt` (`hello world` / `foo`) | `Words: 3` |
@@THEORY
## Слова по пробелам

~~~csharp
string text = File.ReadAllText(path);
string[] words = text.Split(
    new char[] { ' ', '\t', '\r', '\n' },
    StringSplitOptions.RemoveEmptyEntries);
Console.WriteLine($"Words: {words.Length}");
~~~

`Split` с `RemoveEmptyEntries` считает только непустые куски, поэтому
лишние пробелы и пустые строки не увеличивают результат.

## Пустой файл

`File.WriteAllText("empty.txt", "")` создаёт пустой файл. `Split` вернёт
пустой массив, `Length` равно `0`.

## Что считается словом

Здесь словом считается любой набор символов между пробельными. Знаки
препинания остаются частью слова — для точной токенизации нужны
regex или `char.IsLetterOrDigit`.

## Альтернатива

~~~csharp
foreach (string line in File.ReadAllLines(path))
{
    string[] parts = line.Split(' ');
    // ...
}
~~~
@@TESTS
| `text.txt` (`hello world\nfoo\n`) | `Words: 3\n` |
| `text.txt` (`  one   two  `) | `Words: 2\n` |
| `text.txt` (пустой файл) | `Words: 0\n` |
@@CASES
trap 'rm -f text.txt' EXIT
printf 'hello world\nfoo\n' > text.txt
run_case "text.txt" $'Words: 3\n'
printf '  one   two  ' > text.txt
run_case "text.txt" $'Words: 2\n'
: > text.txt
run_case "text.txt" $'Words: 0\n'
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // TODO: посчитай слова в файле
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);
        string[] words = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string text = File.ReadAllText(path);

        // RemoveEmptyEntries не считает пустые куски словами.
        string[] words = text.Split(
            new char[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Words: {words.Length}");
    }
}
@@END

@@TASK
section: 10_files
dir: 06_file_stats
num: 10_6
title: CS_10_06. Статистика файла
topics: `File.ReadAllLines`, строки, символы
input: Имя файла
@@DESC
Выведи статистику файла:

~~~text
Lines: 2
Words: 3
Chars: 13
~~~

- `Lines` — количество строк;
- `Words` — количество слов;
- `Chars` — количество символов без пробельных.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `text.txt` (`hello world` / `foo`) | `Lines: 2`<br>`Words: 3`<br>`Chars: 13` |
@@THEORY
## Построчное чтение

~~~csharp
string[] lines = File.ReadAllLines(path);
~~~

Метод возвращает массив строк без символов перевода строки. Пустой файл
даёт массив длины `0`.

## Слова

~~~csharp
string[] words = line.Split(
    new char[] { ' ', '\t' },
    StringSplitOptions.RemoveEmptyEntries);
~~~

## Символы без пробелов

~~~csharp
foreach (char c in line)
{
    if (!char.IsWhiteSpace(c))
    {
        chars++;
    }
}
~~~

`char.IsWhiteSpace` учитывает пробел, табуляцию и переводы строк.

## Трассировка

Файл `hello world\nfoo\n`:

| Строка | Слов | Символов |
| --- | --- | --- |
| `hello world` | 2 | 10 |
| `foo` | 1 | 3 |

Итого: `Lines: 2`, `Words: 3`, `Chars: 13`.

## Пустой файл

Все три значения равны `0`.
@@TESTS
| `text.txt` (`hello world\nfoo\n`) | `Lines: 2\nWords: 3\nChars: 13\n` |
| `text.txt` (`one\n`) | `Lines: 1\nWords: 1\nChars: 3\n` |
| `text.txt` (пустой файл) | `Lines: 0\nWords: 0\nChars: 0\n` |
@@CASES
trap 'rm -f text.txt' EXIT
printf 'hello world\nfoo\n' > text.txt
run_case "text.txt" $'Lines: 2\nWords: 3\nChars: 13\n'
printf 'one\n' > text.txt
run_case "text.txt" $'Lines: 1\nWords: 1\nChars: 3\n'
: > text.txt
run_case "text.txt" $'Lines: 0\nWords: 0\nChars: 0\n'
@@MAIN
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // TODO: посчитай строки, слова и символы без пробелов
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();
        string[] lines = File.ReadAllLines(path);

        int words = 0;
        int chars = 0;
        foreach (string line in lines)
        {
            words += line.Split(
                new char[] { ' ', '\t' },
                StringSplitOptions.RemoveEmptyEntries).Length;
            foreach (char c in line)
            {
                if (!char.IsWhiteSpace(c))
                {
                    chars++;
                }
            }
        }

        Console.WriteLine($"Lines: {lines.Length}");
        Console.WriteLine($"Words: {words}");
        Console.WriteLine($"Chars: {chars}");
    }
}
@@COMMENTED
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine();

        // ReadAllLines уже делит файл на строки без \n.
        string[] lines = File.ReadAllLines(path);

        int words = 0;
        int chars = 0;
        foreach (string line in lines)
        {
            words += line.Split(
                new char[] { ' ', '\t' },
                StringSplitOptions.RemoveEmptyEntries).Length;
            foreach (char c in line)
            {
                // Пробельные символы в Chars не входят.
                if (!char.IsWhiteSpace(c))
                {
                    chars++;
                }
            }
        }

        Console.WriteLine($"Lines: {lines.Length}");
        Console.WriteLine($"Words: {words}");
        Console.WriteLine($"Chars: {chars}");
    }
}
@@END
