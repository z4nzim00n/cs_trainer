# Разбор задания

## Дробные числа

~~~csharp
double value = double.Parse(line, CultureInfo.InvariantCulture);
~~~

`double` хранит число с плавающей точкой. `CultureInfo.InvariantCulture`
заставляет парсер ожидать точку, а не запятую.

## Формат F2

~~~csharp
string text = value.ToString("F2", CultureInfo.InvariantCulture);
Console.WriteLine("Value: " + text);
~~~

`F2` означает фиксированный формат с двумя знаками после разделителя.
Без `InvariantCulture` на русской Windows получится `3,14`.

## Зачем InvariantCulture

| Культура | Вывод |
| --- | --- |
| Invariant | `3.14` |
| ru-RU | `3,14` |
| de-DE | `3,14` |

Тесты ожидают точку. Поэтому формат задаётся явно.

## Округление

`F2` округляет по правилам .NET. Например, `2.345` может дать `2.35`
или `2.34` из-за двоичного представления `double`. В задачах значения
подобраны без спорных границ.
