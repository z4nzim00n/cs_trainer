# Разбор задания

## Разбор строки

~~~csharp
string[] parts = Console.ReadLine().Split(' ');
int a = int.Parse(parts[0]);
int b = int.Parse(parts[1]);
~~~

Массив `parts` содержит части строки. Индексы начинаются с нуля.

## Сложение

~~~csharp
int sum = a + b;
Console.WriteLine($"Sum: {sum}");
~~~

## Переполнение

`int` хранит примерно от -2 млрд до 2 млрд. Сумма двух больших чисел может
переполниться. Для таких случаев есть `long`:

~~~csharp
long sum = (long)a + b;
~~~

В задаче числа небольшие, но помнить об ограничении полезно.
