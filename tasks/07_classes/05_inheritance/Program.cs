using System;

class Animal
{
    public virtual string Speak()
    {
        return "...";
    }
}

class Dog : Animal
{
}

class Cat : Animal
{
}

class Program
{
    static void Main()
    {
        string kind = Console.ReadLine();

        // TODO: создай нужное животное и выведи его звук
        Console.WriteLine("TODO");
    }
}
