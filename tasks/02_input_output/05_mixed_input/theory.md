# Разбор задания

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
