# Разбор задания

## Слова по пробелам

~~~csharp
string text = File.ReadAllText(path);
string[] words = text.Split(
    new char[] { ' ', '\t', '\r', '\n' },
    StringSplitOptions.RemoveEmptyEntries);
Console.WriteLine($"Words: {words.Length}");
~~~

`Split` с `RemoveEmptyEntries` считает только непустые куски, поэтому
лишние пробелы и пустые строки не увеличивают результат.

## Пустой файл

`File.WriteAllText("empty.txt", "")` создаёт пустой файл. `Split` вернёт
пустой массив, `Length` равно `0`.

## Что считается словом

Здесь словом считается любой набор символов между пробельными. Знаки
препинания остаются частью слова — для точной токенизации нужны
regex или `char.IsLetterOrDigit`.

## Альтернатива

~~~csharp
foreach (string line in File.ReadAllLines(path))
{
    string[] parts = line.Split(' ');
    // ...
}
~~~
