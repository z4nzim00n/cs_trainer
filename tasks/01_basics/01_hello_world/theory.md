# Разбор задания

## Пространства имён

~~~csharp
using System;
~~~

`Console` объявлен в пространстве имён `System`. Без `using System` придётся
писать полное имя `System.Console`.

## Класс и точка входа

~~~csharp
class Program
{
    static void Main()
    {
    }
}
~~~

`Main` — статический метод, с которого начинается выполнение. Компилятор
ищет его среди классов программы. Имя класса `Program` не обязательно, но
так принято.

## Вывод

~~~csharp
Console.WriteLine("Hello, C#!"); // с переводом строки
Console.Write("Hello");          // без перевода строки
~~~

| Метод | Перевод строки |
| --- | --- |
| `Console.Write` | нет |
| `Console.WriteLine` | да |

На Windows `WriteLine` выводит `\r\n`, на Linux/macOS — `\n`. Тесты
нормализуют `\r`, поэтому формат одинаковый на всех платформах.

## Частые ошибки

| Ошибка | Сообщение компилятора |
| --- | --- |
| Нет `using System` | `The name 'Console' does not exist` |
| `Main` не статический | `Main must be static` |
| Нет класса | `Program does not contain a static 'Main' method` |
| Забыта `;` | `; expected` |
