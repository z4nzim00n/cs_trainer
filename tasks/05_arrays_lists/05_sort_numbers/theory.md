# Разбор задания

## Сортировка списка

~~~csharp
numbers.Sort();
~~~

`List<int>.Sort()` сортирует по возрастанию. Для `int` используется
стандартное сравнение.

## Сортировка массива

~~~csharp
Array.Sort(array);
~~~

Для массива вызывается статический метод `Array.Sort`.

## Компаратор

Для другого порядка передайте `Comparison<T>`:

~~~csharp
numbers.Sort((a, b) => b.CompareTo(a)); // по убыванию
~~~

Лямбда возвращает отрицательное число, ноль или положительное — как
`CompareTo`.

## Вывод

~~~csharp
Console.WriteLine(string.Join(" ", numbers));
~~~
