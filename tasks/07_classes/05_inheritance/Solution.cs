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

class Program
{
    static void Main()
    {
        string kind = Console.ReadLine();
        Animal animal = kind == "dog" ? (Animal)new Dog() : new Cat();
        Console.WriteLine(animal.Speak());
    }
}
