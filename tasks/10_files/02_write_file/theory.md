# Разбор задания

## Запись целиком

~~~csharp
File.WriteAllText(path, text);
~~~

Метод создаёт файл или полностью заменяет его содержимое. Каталог
должен существовать.

## Кодировка

По умолчанию `WriteAllText` пишет UTF-8 без BOM. Для явного выбора
есть перегрузка с `Encoding`:

~~~csharp
File.WriteAllText(path, text, Encoding.UTF8);
~~~

## Перевод строки

`WriteAllText` не добавляет `\n` автоматически. Если нужен перевод
строки, добавьте его в строку:

~~~csharp
File.WriteAllText(path, text + Environment.NewLine);
~~~

## Подтверждение

~~~csharp
Console.WriteLine($"Written: {path}");
~~~

## Ошибки

Нет прав или каталога — `UnauthorizedAccessException` или
`DirectoryNotFoundException`. В задаче путь корректен.
