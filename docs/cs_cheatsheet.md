# Шпаргалка по C#

Краткий справочник по темам тренажёра. Синтаксис — C# 7+.

---

## 1. Структура программы

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, C#!");
    }
}
```

- Точка входа — `static void Main()` или `static int Main()`.
- Весь код находится внутри класса или структуры.
- `using` подключает пространство имён.

Несколько пространств имён:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
```

Компиляция одним файлом:

```bash
csc -nologo -langversion:latest -out:app.exe Program.cs
./app.exe
```

В Git Bash используйте дефисные опции: `/nologo` bash примет за путь.

---

## 2. Переменные и типы

```csharp
int x = 42;
double pi = 3.14;
bool ok = true;
char c = 'A';
string s = "text";

var n = 10;          // вывод типа int
const int Limit = 5;
int? maybe = null;    // Nullable<int>
```

| Тип | Размер | Значение по умолчанию |
| --- | --- | --- |
| `int` | 32 бита | `0` |
| `long` | 64 бита | `0` |
| `double` | 64 бита | `0` |
| `decimal` | 128 бит | `0` |
| `bool` | — | `false` |
| `char` | UTF-16 | `'\0'` |
| `string` | ссылочный | `null` |

Приведение:

```csharp
int i = (int)3.9;          // 3
double d = (double)sum / n;
string s = n.ToString();
int n2 = int.Parse("42");
int n3;
bool ok = int.TryParse("abc", out n3); // false
```

---

## 3. Ввод и вывод

```csharp
string line = Console.ReadLine();   // строка без \n, null при EOF
int x = int.Parse(Console.ReadLine());

Console.WriteLine("x = " + x);      // добавляет \n
Console.Write(x);                   // без \n
Console.WriteLine($"x = {x}");      // интерполяция
Console.WriteLine("x = {0}", x);    // форматирование
```

Форматирование чисел:

```csharp
using System.Globalization;

double v = 3.14159;
Console.WriteLine(v.ToString("F2", CultureInfo.InvariantCulture)); // 3.14
```

`InvariantCulture` обязательна: на русской Windows иначе будет запятая.

Чтение нескольких чисел из строки:

```csharp
string[] parts = Console.ReadLine().Split(' ');
int a = int.Parse(parts[0]);
int b = int.Parse(parts[1]);
```

---

## 4. Арифметика и условия

```csharp
7 / 2        // 3
7 % 2        // 1
-7 / 2       // -3
7.0 / 2      // 3.5
Math.PI
Math.Sqrt(x)
Math.Abs(x)
```

`%` работает и для `double`, но для дробных чаще берут `Math.IEEERemainder`.

```csharp
if (x > 0)
{
    // ...
}
else if (x == 0)
{
    // ...
}
else
{
    // ...
}

string kind = x > 0 ? "positive" : "not positive";

switch (day)
{
    case 6:
    case 7:
        Console.WriteLine("weekend");
        break;
    default:
        Console.WriteLine("workday");
        break;
}
```

Логика: `&&`, `||`, `!`. `&&` и `||` используют короткое замыкание.

---

## 5. Циклы

```csharp
for (int i = 0; i < n; ++i)
{
    Console.WriteLine(i);
}

int i = 0;
while (i < n)
{
    i++;
}

do
{
    // выполнится хотя бы раз
} while (false);

foreach (char c in "abc")
{
    Console.WriteLine(c);
}
```

`break` выходит из цикла, `continue` переходит к следующей итерации.

Цифры числа:

```csharp
while (n > 0)
{
    int digit = n % 10;
    n /= 10;
}
```

---

## 6. Массивы и List

```csharp
int[] a = new int[5];          // пять нулей
int[] b = { 1, 2, 3 };
int[,] m = new int[n, n];      // двумерный

List<int> list = new List<int>();
list.Add(4);
list.AddRange(new[] { 5, 6 });
list.Sort();
list.Reverse();
int count = list.Count;
```

- `a.Length` — длина массива, `list.Count` — размер списка.
- Индексация с нуля.
- `List<T>` растёт через `Add`; массив фиксируется при создании.

Вывод:

```csharp
Console.WriteLine(string.Join(" ", list));
```

---

## 7. Строки

Строки неизменяемы: методы возвращают новую строку.

```csharp
string s = "Привет";

s.Length                        // количество char (UTF-16)
s.ToUpperInvariant()
s.ToLowerInvariant()
s.Trim()
s.Contains("ри")
s.StartsWith("Пр")
s.Replace("и", "e")
s.Split(',')
s.Substring(1, 3)
```

Разбиение с удалением пустых кусков:

```csharp
string[] words = line.Split(
    new char[] { ' ', '\t' },
    StringSplitOptions.RemoveEmptyEntries);
```

Разворот:

```csharp
char[] chars = s.ToCharArray();
Array.Reverse(chars);
string reversed = new string(chars);
```

Сравнение: `==` для `string` сравнивает содержимое.

Сборка:

```csharp
var sb = new StringBuilder();
sb.Append("a");
sb.Append("b");
Console.WriteLine(sb.ToString());
```

---

## 8. Классы и объекты

```csharp
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
        return $"({X}, {Y})";
    }
}

Point p = new Point(1, 2);
```

Свойства и `readonly`:

```csharp
class Student
{
    public string Name { get; }
    public readonly int Grade;

    public Student(string name, int grade)
    {
        Name = name;
        Grade = grade;
    }
}
```

Наследование и полиморфизм:

```csharp
class Animal
{
    public virtual string Speak() { return "..."; }
}

class Dog : Animal
{
    public override string Speak() { return "Woof"; }
}

Animal a = new Dog();
Console.WriteLine(a.Speak()); // Woof
```

Абстрактный класс:

```csharp
abstract class Shape
{
    public abstract double Area();
}
```

---

## 9. Коллекции

```csharp
var map = new Dictionary<string, int>();
map["a"] = 1;

if (map.TryGetValue("a", out int value))
{
    Console.WriteLine(value);
}

foreach (var pair in map)
{
    Console.WriteLine($"{pair.Key}: {pair.Value}");
}

var seen = new HashSet<int>();
bool added = seen.Add(5);       // false, если уже было

var sorted = new SortedDictionary<int, string>();
sorted[2] = "b";
```

- Порядок обхода `Dictionary` не определён.
- Для стабильного вывода сортируйте ключи или берите
  `SortedDictionary`.
- `HashSet` хранит уникальные значения.

---

## 10. Исключения, using, defer-аналоги

```csharp
try
{
    int result = a / b;
}
catch (DivideByZeroException)
{
    Console.WriteLine("division by zero");
}
finally
{
    // выполнится всегда
}
```

Своё исключение:

```csharp
class NegativeAgeException : Exception
{
    public NegativeAgeException(string message) : base(message)
    {
    }
}

throw new NegativeAgeException("age cannot be negative");
```

`IDisposable` и `using`:

```csharp
using (var reader = new StreamReader(path))
{
    string text = reader.ReadToEnd();
}
```

`Dispose()` вызывается при выходе из блока даже при исключении.

`TryParse` вместо исключения:

```csharp
if (int.TryParse(input, out int value))
{
    // ...
}
```

---

## 11. Файлы

```csharp
using System.IO;

string text = File.ReadAllText("input.txt");
File.WriteAllText("output.txt", text);
string[] lines = File.ReadAllLines("input.txt");
File.Copy("a.txt", "b.txt", true);
bool exists = File.Exists("input.txt");
```

Построчное чтение большого файла:

```csharp
using (var reader = new StreamReader("input.txt"))
{
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        Console.WriteLine(line);
    }
}
```

Ошибки: `FileNotFoundException`, `DirectoryNotFoundException`,
`IOException`, `UnauthorizedAccessException`.

---

## 12. Потоки и задачи

```csharp
using System.Threading;
using System.Threading.Tasks;

var t = new Thread(() => Console.WriteLine("worker"));
t.Start();
t.Join();
```

`lock`:

```csharp
object gate = new object();

lock (gate)
{
    counter++;
}
```

`Interlocked`:

```csharp
Interlocked.Increment(ref counter);
```

`Task`:

```csharp
Task<int> task = Task.Run(() =>
{
    return 42;
});

Console.WriteLine(task.Result); // блокирует до завершения
```

Несколько задач:

```csharp
Task<long> left = Task.Run(() => Sum(a, 0, mid));
Task<long> right = Task.Run(() => Sum(a, mid, n));
Task.WaitAll(left, right);
long total = left.Result + right.Result;
```

Правила:

- `Join` и `WaitAll` делают порядок детерминированным;
- общий счётчик защищайте `lock` или `Interlocked`;
- не полагайтесь на планировщик в тестах.

---

## 13. Дженерики и LINQ

Обобщённый метод:

```csharp
static T Max<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) >= 0 ? a : b;
}
```

Лямбда-сортировка:

```csharp
words.Sort((x, y) =>
{
    int cmp = x.Length.CompareTo(y.Length);
    return cmp != 0 ? cmp : string.CompareOrdinal(x, y);
});
```

LINQ:

```csharp
using System.Linq;

var result = numbers
    .Where(x => x % 2 == 0)
    .Select(x => x * x)
    .OrderBy(x => x)
    .ToList();

int sum = numbers.Sum();
int max = numbers.Max();
bool any = numbers.Any(x => x > 10);
```

Перегрузка оператора:

```csharp
class Vector
{
    public int X;
    public int Y;

    public Vector(int x, int y)
    {
        X = x;
        Y = y;
    }

    public static Vector operator +(Vector a, Vector b)
    {
        return new Vector(a.X + b.X, a.Y + b.Y);
    }
}
```

---

## 14. Полезные пространства имён

| Пространство | Для чего |
| --- | --- |
| `System` | базовые типы, `Console`, `Math`, `Convert` |
| `System.Collections.Generic` | `List`, `Dictionary`, `HashSet` |
| `System.Linq` | `Where`, `Select`, `OrderBy`, `Sum` |
| `System.IO` | `File`, `Path`, `StreamReader` |
| `System.Text` | `StringBuilder`, `Encoding` |
| `System.Globalization` | `CultureInfo.InvariantCulture` |
| `System.Threading` | `Thread`, `Interlocked` |
| `System.Threading.Tasks` | `Task`, `Task.WaitAll` |

---

## 15. Частые ошибки новичка

| Ошибка | Как правильно |
| --- | --- |
| `Console.ReadLine()` без разбора | `int.Parse(Console.ReadLine())` |
| `sum / n` для среднего | `(double)sum / n` |
| `list.Length` | `list.Count` |
| `array.Count` | `array.Length` |
| `double.ToString("F2")` без культуры | `CultureInfo.InvariantCulture` |
| `if (s == null)` и вызов метода | проверять на `null` |
| `catch (Exception)` первым | сначала конкретные исключения |
| `map[key]` без проверки | `TryGetValue` |
| `counter++` из нескольких потоков | `lock` или `Interlocked` |
| `Dictionary` без сортировки ключей | собрать ключи и `Sort` |
| `foreach` по `Dictionary` с ожиданием порядка | `SortedDictionary` |
| `new int[n]` при `n = 0` и обращение `[0]` | проверять границы |
| `null` вместо пустой строки | `string.IsNullOrEmpty` |
| `==` для объекта без `Equals` | сравнивать поля или переопределить `Equals` |
