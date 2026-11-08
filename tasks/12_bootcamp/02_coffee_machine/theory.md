# Разбор задания

## Состояние

Достаточно двух переменных:

~~~csharp
int water = 0;
int coffee = 0;
~~~

Команды меняют состояние, `cup` проверяет и уменьшает ресурсы.

## Разбор команды

~~~csharp
string[] parts = Console.ReadLine().Split(' ');
if (parts[0] == "water")
{
    water += int.Parse(parts[1]);
}
else if (parts[0] == "coffee")
{
    coffee += int.Parse(parts[1]);
}
else if (parts[0] == "cup")
{
    // ...
}
~~~

## Приготовление

~~~csharp
if (water >= 200 && coffee >= 10)
{
    water -= 200;
    coffee -= 10;
    Console.WriteLine("Coffee ready");
}
else
{
    Console.WriteLine("Not enough resources");
}
~~~

Проверка идёт **до** списания: при нехватке ресурсы не меняются.

## Итог

После всех команд печатаются остатки в формате `Water: X` и
`Coffee: Y`.
