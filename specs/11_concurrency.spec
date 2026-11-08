@@TASK
section: 11_concurrency
dir: 01_thread_basics
num: 11_1
title: CS_11_01. Первый поток
topics: `Thread`, `Start`, `Join`
input: Нет
@@DESC
Запусти поток, который печатает `Hello from thread`, дождись его
завершения и напечатай `Main done`:

~~~text
Hello from thread
Main done
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| — | `Hello from thread`<br>`Main done` |
@@THEORY
## Поток

`Thread` запускает код параллельно с `Main`:

~~~csharp
using System.Threading;

Thread t = new Thread(() =>
{
    Console.WriteLine("Hello from thread");
});
t.Start();
t.Join();
Console.WriteLine("Main done");
~~~

## Методы

- `Start()` — начинает выполнение;
- `Join()` — блокирует текущий поток, пока этот не завершится.

Без `Join` порядок строк был бы случайным: `Main` мог бы закончиться
раньше потока.

## Зачем синхронизация

Тесты сравнивают точный вывод. `Join` делает порядок детерминированным:
сначала строка потока, потом строка главного потока.

## `Thread` или `Task`

`Thread` — низкоуровневый поток ОС. `Task` — задача для пула потоков,
её обычно достаточно. `Thread` полезен, чтобы увидеть основы.
@@TESTS
| (пустой ввод) | `Hello from thread\nMain done\n` |
@@CASES
run_case_devnull $'Hello from thread\nMain done\n'
@@MAIN
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        // TODO: создай поток, запусти, дождись и выведи Main done
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Thread t = new Thread(() =>
        {
            Console.WriteLine("Hello from thread");
        });
        t.Start();
        t.Join();
        Console.WriteLine("Main done");
    }
}
@@COMMENTED
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Thread t = new Thread(() =>
        {
            Console.WriteLine("Hello from thread");
        });
        t.Start();
        // Join гарантирует, что поток закончит до следующей строки.
        t.Join();
        Console.WriteLine("Main done");
    }
}
@@END

@@TASK
section: 11_concurrency
dir: 02_two_threads
num: 11_2
title: CS_11_02. Два потока
topics: `Thread`, общий массив, `Join`
input: Два целых числа `a` и `b`
@@DESC
Посчитай квадраты `a` и `b` в двух разных потоках. Выведи результаты:

~~~text
A: 4
B: 9
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2 3` | `A: 4`<br>`B: 9` |
| `-4 5` | `A: 16`<br>`B: 25` |
@@THEORY
## Результаты в разных ячейках

Если два потока пишут в одну переменную, результат зависит от гонки.
Здесь каждый поток пишет в свою ячейку массива:

~~~csharp
int[] results = new int[2];
Thread t1 = new Thread(() => results[0] = a * a);
Thread t2 = new Thread(() => results[1] = b * b);
t1.Start();
t2.Start();
t1.Join();
t2.Join();
~~~

## Почему это безопасно

Потоки не обращаются к одной памяти на запись. После `Join` обе записи
видны главному потоку.

## Порядок печати

Печатает только главный поток, поэтому `A:` всегда идёт перед `B:`,
несмотря на параллельные вычисления.

## Замыкания

Лямбда захватывает `a` и `b`. В C# захваченные локальные переменные
живут, пока жива лямбда.
@@TESTS
| `2 3` | `A: 4\nB: 9\n` |
| `-4 5` | `A: 16\nB: 25\n` |
| `0 0` | `A: 0\nB: 0\n` |
@@CASES
run_case "2 3" $'A: 4\nB: 9\n'
run_case "-4 5" $'A: 16\nB: 25\n'
run_case "0 0" $'A: 0\nB: 0\n'
@@MAIN
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // TODO: посчитай квадраты в двух потоках
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        int[] results = new int[2];
        Thread t1 = new Thread(() => results[0] = a * a);
        Thread t2 = new Thread(() => results[1] = b * b);
        t1.Start();
        t2.Start();
        t1.Join();
        t2.Join();

        Console.WriteLine($"A: {results[0]}");
        Console.WriteLine($"B: {results[1]}");
    }
}
@@COMMENTED
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        // У каждого потока своя ячейка — общих записей нет.
        int[] results = new int[2];
        Thread t1 = new Thread(() => results[0] = a * a);
        Thread t2 = new Thread(() => results[1] = b * b);
        t1.Start();
        t2.Start();
        t1.Join();
        t2.Join();

        Console.WriteLine($"A: {results[0]}");
        Console.WriteLine($"B: {results[1]}");
    }
}
@@END

@@TASK
section: 11_concurrency
dir: 03_lock_counter
num: 11_3
title: CS_11_03. Счётчик с lock
topics: `lock`, общий счётчик, гонка данных
input: Количество потоков `n` и число инкрементов `m`
@@DESC
Запусти `n` потоков, каждый увеличивает общий счётчик `m` раз.
Выведи итог:

~~~text
Counter: 4000
~~~

Используй `lock`, чтобы не потерять обновления.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4 1000` | `Counter: 4000` |
| `1 5` | `Counter: 5` |
@@THEORY
## Гонка данных

`counter++` — не одна операция, а чтение, сложение и запись. Два потока
могут прочитать одно значение и оба записать `counter + 1`, потеряв
один инкремент.

## `lock`

~~~csharp
object gate = new object();
...
lock (gate)
{
    counter++;
}
~~~

`lock` захватывает объект-монитор. Пока один поток внутри блока, другие
ждут на входе. Обновление становится атомарным.

## Потоки

~~~csharp
Thread[] threads = new Thread[n];
for (int i = 0; i < n; ++i)
{
    threads[i] = new Thread(() =>
    {
        for (int j = 0; j < m; ++j)
        {
            lock (gate) { counter++; }
        }
    });
    threads[i].Start();
}
foreach (Thread t in threads) t.Join();
~~~

## Альтернатива

`Interlocked.Increment(ref counter)` делает то же без явного `lock` и
обычно быстрее. `lock` полезен, когда под защитой несколько операций.

## Правило

Всегда используйте один и тот же объект для одного и того же ресурса.
`lock (this)` опасен: внешний код может захватить тот же объект.
@@TESTS
| `4 1000` | `Counter: 4000\n` |
| `1 5` | `Counter: 5\n` |
| `2 0` | `Counter: 0\n` |
@@CASES
run_case "4 1000" $'Counter: 4000\n'
run_case "1 5" $'Counter: 5\n'
run_case "2 0" $'Counter: 0\n'
@@MAIN
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        int m = int.Parse(parts[1]);

        // TODO: запусти n потоков по m инкрементов с lock
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        int m = int.Parse(parts[1]);

        int counter = 0;
        object gate = new object();
        Thread[] threads = new Thread[n];
        for (int i = 0; i < n; ++i)
        {
            threads[i] = new Thread(() =>
            {
                for (int j = 0; j < m; ++j)
                {
                    lock (gate)
                    {
                        counter++;
                    }
                }
            });
            threads[i].Start();
        }
        foreach (Thread t in threads)
        {
            t.Join();
        }

        Console.WriteLine($"Counter: {counter}");
    }
}
@@COMMENTED
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        string[] parts = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        int m = int.Parse(parts[1]);

        int counter = 0;
        // Один объект-замок на все потоки.
        object gate = new object();
        Thread[] threads = new Thread[n];
        for (int i = 0; i < n; ++i)
        {
            threads[i] = new Thread(() =>
            {
                for (int j = 0; j < m; ++j)
                {
                    lock (gate)
                    {
                        counter++;
                    }
                }
            });
            threads[i].Start();
        }
        foreach (Thread t in threads)
        {
            t.Join();
        }

        Console.WriteLine($"Counter: {counter}");
    }
}
@@END

@@TASK
section: 11_concurrency
dir: 04_task_pipeline
num: 11_4
title: CS_11_04. Задача Task
topics: `Task.Run`, `Result`, пул потоков
input: Число `n`
@@DESC
Вычисли сумму `1 + 2 + ... + n` в задаче и выведи её:

~~~text
Sum: 15
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5` | `Sum: 15` |
| `1` | `Sum: 1` |
@@THEORY
## `Task`

`Task` — единица асинхронной работы. `Task.Run` ставит делегат в пул
потоков:

~~~csharp
using System.Threading.Tasks;

Task<int> task = Task.Run(() =>
{
    int sum = 0;
    for (int i = 1; i <= n; ++i)
    {
        sum += i;
    }
    return sum;
});
~~~

`Task<int>` представляет результат типа `int`.

## Получение результата

~~~csharp
int sum = task.Result;
~~~

Свойство `Result` блокирует вызывающий поток, пока задача не завершится.
Это удобно в консольной программе, но в UI-потоке может привести к
зависанию — там используют `await`.

## `Task` и `Thread`

`Task` переиспользует потоки пула, поэтому создавать тысячи задач
дешевле, чем тысячи `Thread`.

## Исключения

Исключение внутри задачи сохраняется и бросается при `Result` или
`Wait()`, обёрнутое в `AggregateException`.
@@TESTS
| `5` | `Sum: 15\n` |
| `1` | `Sum: 1\n` |
| `100` | `Sum: 5050\n` |
@@CASES
run_case "5" $'Sum: 15\n'
run_case "1" $'Sum: 1\n'
run_case "100" $'Sum: 5050\n'
@@MAIN
using System;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        // TODO: посчитай сумму в Task и выведи её
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        Task<int> task = Task.Run(() =>
        {
            int sum = 0;
            for (int i = 1; i <= n; ++i)
            {
                sum += i;
            }
            return sum;
        });

        Console.WriteLine($"Sum: {task.Result}");
    }
}
@@COMMENTED
using System;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        Task<int> task = Task.Run(() =>
        {
            int sum = 0;
            for (int i = 1; i <= n; ++i)
            {
                sum += i;
            }
            return sum;
        });

        // Result ждёт завершения задачи и возвращает значение.
        Console.WriteLine($"Sum: {task.Result}");
    }
}
@@END

@@TASK
section: 11_concurrency
dir: 05_parallel_sum
num: 11_5
title: CS_11_05. Параллельная сумма
topics: `Task`, `Task.WaitAll`, разбиение массива
input: `n`, затем `n` целых чисел
@@DESC
Раздели массив на две половины, сложи каждую в отдельной задаче и
выведи общий результат:

~~~text
Sum: 15
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `Sum: 15` |
| `4`<br>`-1 10 -2 3` | `Sum: 10` |
@@THEORY
## Разбиение

~~~csharp
int mid = n / 2;
Task<long> left = Task.Run(() => Sum(numbers, 0, mid));
Task<long> right = Task.Run(() => Sum(numbers, mid, n));
Task.WaitAll(left, right);
long total = left.Result + right.Result;
~~~

Каждая задача обрабатывает свой диапазон `[from, to)` и не пишет в общую
память. Это безопасно без `lock`.

## `WaitAll`

~~~csharp
Task.WaitAll(left, right);
~~~

Блокирует поток до завершения всех задач. После этого `Result` уже
готов и не ждёт.

## Вспомогательный метод

~~~csharp
static long Sum(int[] numbers, int from, int to)
{
    long sum = 0;
    for (int i = from; i < to; ++i)
    {
        sum += numbers[i];
    }
    return sum;
}
~~~

## Крайние случаи

- `n = 1`: одна половина пустая, вторая содержит единственный элемент.
- `n = 0`: обе половины пустые, сумма `0`.

`long` защищает от переполнения при больших значениях.
@@TESTS
| `5\n1 2 3 4 5` | `Sum: 15\n` |
| `4\n-1 10 -2 3` | `Sum: 10\n` |
| `1\n7` | `Sum: 7\n` |
| `0\n` | `Sum: 0\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'Sum: 15\n'
run_case $'4\n-1 10 -2 3' $'Sum: 10\n'
run_case $'1\n7' $'Sum: 7\n'
run_case $'0\n' $'Sum: 0\n'
@@MAIN
using System;
using System.Threading.Tasks;

class Program
{
    static long Sum(int[] numbers, int from, int to)
    {
        // TODO: сложи элементы диапазона
        return 0;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        // TODO: сложи две половины в задачах
        Console.WriteLine("TODO");
    }
}
@@SOLUTION
using System;
using System.Threading.Tasks;

class Program
{
    static long Sum(int[] numbers, int from, int to)
    {
        long sum = 0;
        for (int i = from; i < to; ++i)
        {
            sum += numbers[i];
        }
        return sum;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int mid = n / 2;
        Task<long> left = Task.Run(() => Sum(numbers, 0, mid));
        Task<long> right = Task.Run(() => Sum(numbers, mid, n));
        Task.WaitAll(left, right);

        Console.WriteLine($"Sum: {left.Result + right.Result}");
    }
}
@@COMMENTED
using System;
using System.Threading.Tasks;

class Program
{
    static long Sum(int[] numbers, int from, int to)
    {
        // Диапазон [from, to) — половина массива.
        long sum = 0;
        for (int i = from; i < to; ++i)
        {
            sum += numbers[i];
        }
        return sum;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] parts = Console.ReadLine().Split(' ');
        int[] numbers = new int[n];
        for (int i = 0; i < n; ++i)
        {
            numbers[i] = int.Parse(parts[i]);
        }

        int mid = n / 2;
        Task<long> left = Task.Run(() => Sum(numbers, 0, mid));
        Task<long> right = Task.Run(() => Sum(numbers, mid, n));
        Task.WaitAll(left, right);

        Console.WriteLine($"Sum: {left.Result + right.Result}");
    }
}
@@END
