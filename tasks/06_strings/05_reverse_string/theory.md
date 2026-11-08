# Разбор задания

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
