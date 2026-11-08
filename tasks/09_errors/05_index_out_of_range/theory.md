# Разбор задания

## Границы массива

Массив из `n` элементов имеет индексы `0..n-1`. Обращение к `numbers[n]`
или `numbers[-1]` бросает `IndexOutOfRangeException`.

## Перехват

~~~csharp
try
{
    int value = numbers[index];
    Console.WriteLine($"Value: {value}");
}
catch (IndexOutOfRangeException)
{
    Console.WriteLine("Error: index out of range");
}
~~~

## Массив или список

У `List<T>` индексатор бросает `ArgumentOutOfRangeException`, а не
`IndexOutOfRangeException`. Поэтому здесь используется массив `int[]`, и
тип в `catch` совпадает.

## Проверка заранее

~~~csharp
if (index >= 0 && index < numbers.Length)
{
    // безопасно
}
~~~

Явная проверка дешевле исключения. `try`/`catch` уместен, когда индекс
приходит из ненадёжного источника и проверок много.

## Пустой массив

При `n = 0` любой индекс некорректен, включая `0`.
