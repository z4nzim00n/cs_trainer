# Разбор задания

## Копирование

~~~csharp
File.Copy(source, destination, true);
~~~

Третий аргумент `overwrite: true` разрешает заменить существующий файл.
Без него при наличии файла бросается `IOException`.

## Проверка

После копирования содержимое должно совпадать:

~~~csharp
string original = File.ReadAllText(source);
string copy = File.ReadAllText(destination);
bool same = original == copy;
~~~

## Отличие от перемещения

`File.Move` переносит файл, исходный исчезает. `File.Copy` оставляет
оба.

## Ошибки

- исходного файла нет — `FileNotFoundException`;
- нет прав на запись — `UnauthorizedAccessException`;
- destination указывает на каталог — `IOException`.
