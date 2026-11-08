# Разбор задания

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
