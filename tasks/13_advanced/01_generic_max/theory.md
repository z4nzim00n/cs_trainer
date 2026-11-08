# Разбор задания

## Зачем дженерики

Один алгоритм должен работать для разных типов. Без дженериков
пришлось бы писать `MaxInt`, `MaxString`, `MaxDouble`.

## Обобщённый метод

~~~csharp
static T Max<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) >= 0 ? a : b;
}
~~~

- `<T>` — параметр типа, задаётся при вызове;
- `where T : IComparable<T>` — ограничение: у `T` обязан быть метод
  `CompareTo`.

## Вызов

~~~csharp
int maxInt = Max(3, 7);
string maxString = Max("apple", "banana");
~~~

Компилятор выводит `T` из аргументов: `int` и `string`.

## Ограничения

Без `where` нельзя вызвать `CompareTo`: компилятор не знает, что у `T`
есть такой метод. `IComparable<T>` — стандартный интерфейс сравнения.

## Осторожно со строками

`CompareTo` для `string` зависит от культуры. Для машинного сравнения
используют `string.CompareOrdinal`.
