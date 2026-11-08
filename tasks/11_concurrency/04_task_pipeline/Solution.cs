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
