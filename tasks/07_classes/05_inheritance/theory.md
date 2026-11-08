# Разбор задания

## Базовый класс

~~~csharp
class Animal
{
    public virtual string Speak()
    {
        return "...";
    }
}
~~~

`virtual` разрешает наследникам заменить реализацию.

## Наследник

~~~csharp
class Dog : Animal
{
    public override string Speak()
    {
        return "Woof";
    }
}

class Cat : Animal
{
    public override string Speak()
    {
        return "Meow";
    }
}
~~~

Двоеточие означает наследование. `override` обязателен при замене
виртуального метода.

## Полиморфизм

~~~csharp
Animal animal = new Dog();
Console.WriteLine(animal.Speak());
~~~

Переменная типа `Animal` хранит `Dog`, и вызывается версия `Dog`.
Компилятор выбирает метод по фактическому типу объекта.

## Выбор объекта

~~~csharp
Animal animal = kind == "dog" ? (Animal)new Dog() : new Cat();
~~~

Тернарный оператор требует общего типа, поэтому приведение к `Animal`
убирает неоднозначность.
