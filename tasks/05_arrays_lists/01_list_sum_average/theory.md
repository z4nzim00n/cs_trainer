# Разбор задания

## Список

~~~csharp
var numbers = new List<int>();
for (int i = 0; i < n; ++i)
{
    numbers.Add(int.Parse(parts[i]));
}
~~~

`List<int>` — динамический массив. В отличие от `int[]`, его размер можно
увеличивать через `Add`.

## Сумма

~~~csharp
long sum = 0;
foreach (int x in numbers)
{
    sum += x;
}
~~~

`long` защищает от переполнения при больших значениях.

## Среднее

~~~csharp
double average = (double)sum / n;
~~~

Приведение к `double` обязательно: `sum / n` для целых даст целое число.

## Формат

~~~csharp
Console.WriteLine("Sum: " + sum);
Console.WriteLine("Average: " + average.ToString("F2", CultureInfo.InvariantCulture));
~~~

## Пустой список

При `n = 0` среднее не определено. В задаче `n > 0`.
