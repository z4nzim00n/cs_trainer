# Разбор задания

## Один проход

Все четыре значения можно найти за один цикл:

~~~csharp
int min = int.MaxValue;
int max = int.MinValue;
long sum = 0;
foreach (int x in numbers)
{
    if (x < min) min = x;
    if (x > max) max = x;
    sum += x;
}
double average = (double)sum / n;
~~~

## Среднее

Приведение к `double` обязательно, иначе `sum / n` отбросит дробную
часть.

## Формат

~~~csharp
using System.Globalization;
...
average.ToString("F2", CultureInfo.InvariantCulture)
~~~

`F2` — ровно два знака. `InvariantCulture` печатает точку.

## Пустой список

При `n = 0` минимум, максимум и среднее не определены. В задаче `n > 0`.
