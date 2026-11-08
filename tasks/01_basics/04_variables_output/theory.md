# Разбор задания

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
