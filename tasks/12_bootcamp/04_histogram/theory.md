# Разбор задания

## Подсчёт

~~~csharp
var counts = new SortedDictionary<int, int>();
foreach (int x in numbers)
{
    if (counts.ContainsKey(x))
    {
        counts[x]++;
    }
    else
    {
        counts[x] = 1;
    }
}
~~~

`SortedDictionary` хранит значения по возрастанию, поэтому вывод сразу
упорядочен.

## Повторение строки

~~~csharp
string stars = new string('*', counts[value]);
Console.WriteLine($"{value}: {stars}");
~~~

`new string(char, count)` создаёт строку из повторённого символа — это
быстрее, чем конкатенация в цикле.

## Только встретившиеся значения

Мы не печатаем нулевые строки для отсутствующих цифр. Если нужна
фиксированная шкала `0..9`, цикл идёт по всем десяти значениям и
печатает пустую строку звёзд.

## Сложность

Подсчёт `O(n log 10)`, фактически `O(n)`: различных цифр не больше
десяти.
