# Разбор задания

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
