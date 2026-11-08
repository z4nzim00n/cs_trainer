# Разбор задания

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
