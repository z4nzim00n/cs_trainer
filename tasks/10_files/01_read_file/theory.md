# Разбор задания

## `System.IO`

Классы для файлов лежат в пространстве имён `System.IO`:

~~~csharp
using System.IO;
~~~

## Чтение целиком

~~~csharp
string text = File.ReadAllText(path);
Console.Write(text);
~~~

`ReadAllText` возвращает строку со всеми переводами строк. `Console.Write`
печатает её без добавления своего `\n` — содержимое останется точным.

## Файла нет

`ReadAllText` бросает `FileNotFoundException`:

~~~csharp
try
{
    string text = File.ReadAllText(path);
    Console.Write(text);
}
catch (FileNotFoundException)
{
    Console.WriteLine("Error: file not found");
}
~~~

## Путь

Относительный путь считается от текущего каталога процесса. В тестах
это папка задания.
