@@TASK
section: 07_classes
dir: 01_first_class
num: 7_1
title: CS_07_01. Первый класс
topics: класс, поля, конструктор, `new`
input: Два целых числа `x` и `y`
@@DESC
Опиши класс `Point` с полями `X` и `Y`, создай объект и выведи его:

~~~text
(3, 4)
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 4` | `(3, 4)` |
| `-1 0` | `(-1, 0)` |
@@THEORY
## Зачем класс

Класс объединяет данные и поведение. В C# код программы тоже находится
внутри класса:

~~~csharp
class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}
~~~

- `public` — поле доступно снаружи класса.
- Конструктор называется как класс и вызывается через `new`.
- `this` не обязателен, если имена не совпадают.

## Создание объекта

~~~csharp
Point p = new Point(x, y);
~~~

`p` хранит ссылку на объект в управляемой куче. Сборщик мусора освободит
память автоматически.

## Поля и свойства

Поле — переменная внутри класса. Свойство (`public int X { get; set; }`)
добавляет методы доступа и позволяет валидировать значения. В этой задаче
достаточно полей.

## Вывод

~~~csharp
Console.WriteLine($"({p.X}, {p.Y})");
~~~
@@TESTS
| `3 4` | `(3, 4)\n` |
| `-1 0` | `(-1, 0)\n` |
| `0 0` | `(0, 0)\n` |
@@CASES
run_case "3 4" $'(3, 4)\n'
run_case "-1 0" $'(-1, 0)\n'
run_case "0 0" $'(0, 0)\n'
@@MAIN
using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        // TODO: создай Point и выведи его координаты
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        Point p = new Point(x, y);
        Console.WriteLine($"({p.X}, {p.Y})");
    }
}
@@COMMENTED
using System;

class Point
{
    public int X;
    public int Y;

    // Конструктор заполняет поля при создании объекта.
    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        Point p = new Point(x, y);
        Console.WriteLine($"({p.X}, {p.Y})");
    }
}
@@END

@@TASK
section: 07_classes
dir: 02_methods_area
num: 7_2
title: CS_07_02. Метод площади
topics: класс, метод, `int`
input: Ширина и высота прямоугольника
@@DESC
Опиши класс `Rectangle` с методом `Area()` и выведи площадь:

~~~text
Area: 12
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 4` | `Area: 12` |
| `5 2` | `Area: 10` |
@@THEORY
## Метод экземпляра

Метод объявляется внутри класса и имеет доступ к его полям:

~~~csharp
class Rectangle
{
    public int Width;
    public int Height;

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int Area()
    {
        return Width * Height;
    }
}
~~~

## Вызов

~~~csharp
Rectangle r = new Rectangle(w, h);
Console.WriteLine($"Area: {r.Area()}");
~~~

Скобки обязательны: `r.Area` без `()` — это группа методов, а не число.

## `static` или экземпляр

`static`-метод не имеет доступа к полям объекта и вызывается через имя
класса. `Area()` зависит от конкретного прямоугольника, поэтому метод
экземпляра.

## Переполнение

`int` хватает для небольших сторон. Для больших значений используйте
`long`, иначе произведение переполнится молча.
@@TESTS
| `3 4` | `Area: 12\n` |
| `5 2` | `Area: 10\n` |
| `1 1` | `Area: 1\n` |
@@CASES
run_case "3 4" $'Area: 12\n'
run_case "5 2" $'Area: 10\n'
run_case "1 1" $'Area: 1\n'
@@MAIN
using System;

class Rectangle
{
    public int Width;
    public int Height;

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int Area()
    {
        // TODO: верни площадь
        return 0;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int w = int.Parse(parts[0]);
        int h = int.Parse(parts[1]);

        // TODO: создай Rectangle и выведи Area
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;

class Rectangle
{
    public int Width;
    public int Height;

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int Area()
    {
        return Width * Height;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int w = int.Parse(parts[0]);
        int h = int.Parse(parts[1]);

        Rectangle r = new Rectangle(w, h);
        Console.WriteLine($"Area: {r.Area()}");
    }
}
@@COMMENTED
using System;

class Rectangle
{
    public int Width;
    public int Height;

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    // Метод экземпляра видит поля текущего объекта.
    public int Area()
    {
        return Width * Height;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int w = int.Parse(parts[0]);
        int h = int.Parse(parts[1]);

        Rectangle r = new Rectangle(w, h);
        Console.WriteLine($"Area: {r.Area()}");
    }
}
@@END

@@TASK
section: 07_classes
dir: 03_constructor
num: 7_3
title: CS_07_03. Конструктор и свойства
topics: конструктор, свойства `get`, `readonly`
input: Имя и оценка
@@DESC
Опиши класс `Student` с полями `Name` и `Grade`, создай объект и выведи:

~~~text
Student: Bob, Grade: 5
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `Bob 5` | `Student: Bob, Grade: 5` |
| `Alice 4` | `Student: Alice, Grade: 4` |
@@THEORY
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
@@TESTS
| `Bob 5` | `Student: Bob, Grade: 5\n` |
| `Alice 4` | `Student: Alice, Grade: 4\n` |
| `Eve 3` | `Student: Eve, Grade: 3\n` |
@@CASES
run_case "Bob 5" $'Student: Bob, Grade: 5\n'
run_case "Alice 4" $'Student: Alice, Grade: 4\n'
run_case "Eve 3" $'Student: Eve, Grade: 3\n'
@@MAIN
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
@@SOLUTION
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

        Student s = new Student(name, grade);
        Console.WriteLine($"Student: {s.Name}, Grade: {s.Grade}");
    }
}
@@COMMENTED
using System;

class Student
{
    // readonly можно присвоить только в конструкторе.
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

        Student s = new Student(name, grade);
        Console.WriteLine($"Student: {s.Name}, Grade: {s.Grade}");
    }
}
@@END

@@TASK
section: 07_classes
dir: 04_to_string_override
num: 7_4
title: CS_07_04. Переопределение ToString
topics: `override`, `ToString`, интерполяция
input: Два целых числа `x` и `y`
@@DESC
Переопредели `ToString()` у класса `Point` так, чтобы `Console.WriteLine(p)`
печатал:

~~~text
Point(1, 2)
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1 2` | `Point(1, 2)` |
| `-3 7` | `Point(-3, 7)` |
@@THEORY
## `ToString` у объекта

`Console.WriteLine(object)` вызывает `ToString()`. По умолчанию возвращается
полное имя типа, например `Point`.

## Переопределение

~~~csharp
class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public override string ToString()
    {
        return $"Point({X}, {Y})";
    }
}
~~~

- `override` обязателен: метод уже объявлен в `object`.
- Сигнатура должна совпадать: `public override string ToString()`.
- `Console.WriteLine($"...{p}")` тоже использует `ToString()`.

## Зачем

Единый текстовый вид объекта удобен для отладки, логов и вывода в консоль.
@@TESTS
| `1 2` | `Point(1, 2)\n` |
| `-3 7` | `Point(-3, 7)\n` |
| `0 0` | `Point(0, 0)\n` |
@@CASES
run_case "1 2" $'Point(1, 2)\n'
run_case "-3 7" $'Point(-3, 7)\n'
run_case "0 0" $'Point(0, 0)\n'
@@MAIN
using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    // TODO: переопредели ToString
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        Point p = new Point(x, y);
        Console.WriteLine(p);
    }
}
@@SOLUTION
using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public override string ToString()
    {
        return $"Point({X}, {Y})";
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        Point p = new Point(x, y);
        Console.WriteLine(p);
    }
}
@@COMMENTED
using System;

class Point
{
    public int X;
    public int Y;

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    // WriteLine(p) вызывает именно этот метод.
    public override string ToString()
    {
        return $"Point({X}, {Y})";
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);

        Point p = new Point(x, y);
        Console.WriteLine(p);
    }
}
@@END

@@TASK
section: 07_classes
dir: 05_inheritance
num: 7_5
title: CS_07_05. Наследование
topics: базовый класс, `virtual`, `override`, полиморфизм
input: `dog` или `cat`
@@DESC
Опиши базовый класс `Animal` с виртуальным методом `Speak()` и наследников
`Dog` и `Cat`. Выведи звук животного:

~~~text
Woof
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `dog` | `Woof` |
| `cat` | `Meow` |
@@THEORY
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
@@TESTS
| `dog` | `Woof\n` |
| `cat` | `Meow\n` |
@@CASES
run_case "dog" $'Woof\n'
run_case "cat" $'Meow\n'
@@MAIN
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
@@SOLUTION
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
@@COMMENTED
using System;

class Animal
{
    // virtual разрешает наследникам переопределить метод.
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

        // Переменная базового типа вызывает метод фактического объекта.
        Animal animal = kind == "dog" ? (Animal)new Dog() : new Cat();
        Console.WriteLine(animal.Speak());
    }
}
@@END

@@TASK
section: 07_classes
dir: 06_abstract_shape
num: 7_6
title: CS_07_06. Абстрактная фигура
topics: `abstract`, `override`, `double`, `F2`
input: `circle R` или `rect W H`
@@DESC
Опиши абстрактный класс `Shape` с методом `Area()` и наследников
`Circle` и `Rectangle`. Выведи площадь с двумя знаками:

~~~text
Area: 12.57
~~~

Для круга используй `Math.PI * R * R`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `circle 2` | `Area: 12.57` |
| `rect 3 4` | `Area: 12.00` |
@@THEORY
## Абстрактный класс

~~~csharp
abstract class Shape
{
    public abstract double Area();
}
~~~

У метода нет тела: каждый наследник обязан его реализовать. Создать
`new Shape()` нельзя — это ошибка компиляции.

## Наследники

~~~csharp
class Circle : Shape
{
    public double R;

    public Circle(double r)
    {
        R = r;
    }

    public override double Area()
    {
        return Math.PI * R * R;
    }
}
~~~

## Полиморфный вызов

~~~csharp
Shape shape = new Circle(r);
double area = shape.Area();
~~~

`Shape` задаёт контракт, наследники — конкретную формулу.

## Формат числа

~~~csharp
using System.Globalization;
...
area.ToString("F2", CultureInfo.InvariantCulture)
~~~

`F2` — два знака после точки. `InvariantCulture` гарантирует точку,
а не запятую.

## Разбор ввода

~~~csharp
string[] parts = line.Split(' ');
if (parts[0] == "circle") { ... }
else { ... }
~~~
@@TESTS
| `circle 2` | `Area: 12.57\n` |
| `rect 3 4` | `Area: 12.00\n` |
| `circle 1` | `Area: 3.14\n` |
@@CASES
run_case "circle 2" $'Area: 12.57\n'
run_case "rect 3 4" $'Area: 12.00\n'
run_case "circle 1" $'Area: 3.14\n'
@@MAIN
using System;
using System.Globalization;

abstract class Shape
{
    public abstract double Area();
}

class Circle : Shape
{
    public double R;

    public Circle(double r)
    {
        R = r;
    }

    public override double Area()
    {
        // TODO: верни площадь круга
        return 0;
    }
}

class Rectangle : Shape
{
    public double W;
    public double H;

    public Rectangle(double w, double h)
    {
        W = w;
        H = h;
    }

    public override double Area()
    {
        // TODO: верни площадь прямоугольника
        return 0;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');

        // TODO: создай нужную фигуру и выведи Area: X.XX
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Globalization;

abstract class Shape
{
    public abstract double Area();
}

class Circle : Shape
{
    public double R;

    public Circle(double r)
    {
        R = r;
    }

    public override double Area()
    {
        return Math.PI * R * R;
    }
}

class Rectangle : Shape
{
    public double W;
    public double H;

    public Rectangle(double w, double h)
    {
        W = w;
        H = h;
    }

    public override double Area()
    {
        return W * H;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Shape shape;
        if (parts[0] == "circle")
        {
            double r = double.Parse(parts[1], CultureInfo.InvariantCulture);
            shape = new Circle(r);
        }
        else
        {
            double w = double.Parse(parts[1], CultureInfo.InvariantCulture);
            double h = double.Parse(parts[2], CultureInfo.InvariantCulture);
            shape = new Rectangle(w, h);
        }

        string area = shape.Area().ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine($"Area: {area}");
    }
}
@@COMMENTED
using System;
using System.Globalization;

abstract class Shape
{
    // Абстрактный метод без тела: контракт для наследников.
    public abstract double Area();
}

class Circle : Shape
{
    public double R;

    public Circle(double r)
    {
        R = r;
    }

    public override double Area()
    {
        return Math.PI * R * R;
    }
}

class Rectangle : Shape
{
    public double W;
    public double H;

    public Rectangle(double w, double h)
    {
        W = w;
        H = h;
    }

    public override double Area()
    {
        return W * H;
    }
}

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        Shape shape;
        if (parts[0] == "circle")
        {
            double r = double.Parse(parts[1], CultureInfo.InvariantCulture);
            shape = new Circle(r);
        }
        else
        {
            double w = double.Parse(parts[1], CultureInfo.InvariantCulture);
            double h = double.Parse(parts[2], CultureInfo.InvariantCulture);
            shape = new Rectangle(w, h);
        }

        // F2 и InvariantCulture дают точку и ровно два знака.
        string area = shape.Area().ToString("F2", CultureInfo.InvariantCulture);
        Console.WriteLine($"Area: {area}");
    }
}
@@END
