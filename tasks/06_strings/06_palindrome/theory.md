# Разбор задания

## Идея

Палиндром — строка, которая совпадает со своим разворотом.

~~~csharp
char[] chars = line.ToCharArray();
Array.Reverse(chars);
string reversed = new string(chars);
Console.WriteLine(line == reversed);
~~~

## Сравнение строк

В C# `==` для `string` сравнивает **содержимое**, а не ссылки. Это
отличается от Java, где `==` сравнивает ссылки.

## Логическое значение

`line == reversed` имеет тип `bool`. `Console.WriteLine` печатает его
как `True` или `False` — с заглавной буквы.

## Без копирования

Можно идти с двух концов:

~~~csharp
int i = 0;
int j = line.Length - 1;
while (i < j && line[i] == line[j])
{
    i++;
    j--;
}
bool ok = i >= j;
~~~
