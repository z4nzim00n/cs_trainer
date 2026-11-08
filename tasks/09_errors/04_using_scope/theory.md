# Разбор задания

## `IDisposable`

Интерфейс с одним методом:

~~~csharp
class Resource : IDisposable
{
    private readonly string name;

    public Resource(string name)
    {
        this.name = name;
        Console.WriteLine($"Open: {name}");
    }

    public void Dispose()
    {
        Console.WriteLine($"Close: {name}");
    }
}
~~~

## `using`

~~~csharp
using (Resource r = new Resource(name))
{
    Console.WriteLine($"Use: {name}");
}
~~~

`using` вызывает `Dispose()` при выходе из блока, даже если внутри
произошло исключение. Это аналог `try/finally`.

## Порядок вызовов

1. Конструктор — `Open`.
2. Тело блока — `Use`.
3. `Dispose` — `Close`.

Такой порядок детерминирован, поэтому его удобно проверять тестами.

## Сокращённая запись

С C# 8 можно писать `using Resource r = new Resource(name);` — `Dispose`
вызовется в конце области видимости.
