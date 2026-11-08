# Разбор задания

## Порядок проверок

Сначала проверяем кратность `15` (или одновременно `3` и `5`), потом `3`,
потом `5`:

~~~csharp
for (int i = 1; i <= n; ++i)
{
    if (i % 15 == 0)
    {
        Console.WriteLine("FizzBuzz");
    }
    else if (i % 3 == 0)
    {
        Console.WriteLine("Fizz");
    }
    else if (i % 5 == 0)
    {
        Console.WriteLine("Buzz");
    }
    else
    {
        Console.WriteLine(i);
    }
}
~~~

Если проверить `3` раньше `15`, число `15` напечатает `Fizz`, а не `FizzBuzz`.

## Почему 15

`15` — наименьшее общее кратное `3` и `5`. Проверка `i % 15 == 0`
эквивалентна `i % 3 == 0 && i % 5 == 0`.

## Вывод числа

`Console.WriteLine(i)` автоматически вызывает `ToString`.
