# Разбор задания

## Исключение при делении

Целочисленное деление на ноль бросает `DivideByZeroException`. Без
обработки программа завершится с ошибкой.

## `try` / `catch`

~~~csharp
try
{
    int result = a / b;
    Console.WriteLine($"Result: {result}");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Error: division by zero");
}
~~~

Код в `try` выполняется, пока не возникнет исключение. Управление
переходит в подходящий `catch`.

## Порядок `catch`

`catch` проверяются сверху вниз, срабатывает первый подходящий. Более
общие исключения (`Exception`) ставьте последними.

## Альтернатива без исключения

~~~csharp
if (b == 0)
{
    Console.WriteLine("Error: division by zero");
}
else
{
    Console.WriteLine($"Result: {a / b}");
}
~~~

Проверка дешевле исключения, но `try`/`catch` показывает механизм,
который нужен для непредсказуемых ошибок.

## Отрицательные числа

Деление целых в C# отбрасывает дробную часть к нулю: `-7 / 2 == -3`.
