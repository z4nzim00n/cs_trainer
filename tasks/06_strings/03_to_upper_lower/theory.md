# Разбор задания

## Смена регистра

~~~csharp
string upper = line.ToUpperInvariant();
string lower = line.ToLowerInvariant();
~~~

Методы возвращают **новую** строку: `string` неизменяем.

## Почему Invariant

`ToUpper()` и `ToLower()` зависят от текущей культуры. В турецкой локали
`i` превращается в `İ`, и тесты могут не совпасть. `Invariant` использует
нейтральные правила и даёт одинаковый результат на любой машине.

## Цифры и знаки

Регистр меняется только у букв. `#`, пробелы, цифры остаются как были.

## Вывод

~~~csharp
Console.WriteLine($"UPPER: {upper}");
Console.WriteLine($"lower: {lower}");
~~~
