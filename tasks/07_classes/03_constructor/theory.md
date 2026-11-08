# Разбор задания

## Свойство только для чтения

Если значение задаётся один раз в конструкторе, поле можно объявить
`readonly`:

~~~csharp
class Student
{
    public readonly string Name;
    public readonly int Grade;

    public Student(string name, int grade)
    {
        Name = name;
        Grade = grade;
    }
}
~~~

`readonly` запрещает менять поле после конструктора. Компилятор поймает
случайную запись `s.Name = ...`.

## Свойство с `get`

Эквивалент — автосвойство только для чтения:

~~~csharp
public string Name { get; }
~~~

Присвоить его можно только в конструкторе.

## Создание

~~~csharp
Student s = new Student(name, grade);
Console.WriteLine($"Student: {s.Name}, Grade: {s.Grade}");
~~~

## Почему не публичные поля

Поля раскрывают внутреннее устройство. Свойства позволяют позже добавить
проверку или вычисление, не меняя код снаружи.
