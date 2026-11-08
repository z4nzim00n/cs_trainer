# Разбор задания

## Свой класс исключения

~~~csharp
class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}
~~~

Наследование от `Exception` делает класс бросаемым. Конструктор передаёт
сообщение в базовый класс, его вернёт свойство `Message`.

## Бросок

~~~csharp
if (age < 0)
{
    throw new NegativeAgeException("age cannot be negative");
}
~~~

`throw` прерывает текущий метод и ищет подходящий `catch` выше по стеку.

## Перехват конкретного типа

~~~csharp
try
{
    // ...
}
catch (NegativeAgeException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}
~~~

## Зачем свои исключения

Тип исключения говорит, что именно пошло не так. Вызывающий код может
обработать `NegativeAgeException` отдельно от остальных ошибок.

## Соглашение об именах

Имена классов исключений заканчиваются на `Exception`.
