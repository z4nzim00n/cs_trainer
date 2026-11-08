# Разбор задания

## Формула

~~~csharp
double area = Math.PI * radius * radius;
~~~

`Math.PI` — константа π с достаточной точностью. `Math.Pow(radius, 2)`
тоже подходит, но умножение проще и быстрее.

## Ввод и вывод

~~~csharp
double radius = double.Parse(line, CultureInfo.InvariantCulture);
string text = area.ToString("F2", CultureInfo.InvariantCulture);
Console.WriteLine("Area: " + text);
~~~

## Порядок операций

`Math.PI * radius * radius` вычисляется слева направо:
`(π · r) · r`. Это то же самое, что `π · r²`.

## Ошибки

- Забыли `InvariantCulture` — на русской Windows получится `12,57`.
- Использовали `float` — точности меньше, но для двух знаков обычно хватает.
- Перепутали радиус и диаметр — площадь отличается в четыре раза.
