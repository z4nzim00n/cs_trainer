using System;

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

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        string name = parts[0];
        int grade = int.Parse(parts[1]);

        // TODO: создай Student и выведи строку
        Console.WriteLine("TODO");
    }
}
