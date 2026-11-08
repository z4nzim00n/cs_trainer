using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int water = 0;
        int coffee = 0;

        for (int i = 0; i < n; ++i)
        {
            string[] parts = Console.ReadLine().Split(' ');
            if (parts[0] == "water")
            {
                water += int.Parse(parts[1]);
            }
            else if (parts[0] == "coffee")
            {
                coffee += int.Parse(parts[1]);
            }
            else if (parts[0] == "cup")
            {
                // Сначала проверка, потом списание.
                if (water >= 200 && coffee >= 10)
                {
                    water -= 200;
                    coffee -= 10;
                    Console.WriteLine("Coffee ready");
                }
                else
                {
                    Console.WriteLine("Not enough resources");
                }
            }
        }

        Console.WriteLine($"Water: {water}");
        Console.WriteLine($"Coffee: {coffee}");
    }
}
