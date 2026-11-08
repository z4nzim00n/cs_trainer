using System;

class Program
{
    static string Shift(string text, int k)
    {
        k = ((k % 26) + 26) % 26;
        char[] chars = text.ToCharArray();
        for (int i = 0; i < chars.Length; ++i)
        {
            char c = chars[i];
            if (c >= 'a' && c <= 'z')
            {
                chars[i] = (char)('a' + (c - 'a' + k) % 26);
            }
            else if (c >= 'A' && c <= 'Z')
            {
                chars[i] = (char)('A' + (c - 'A' + k) % 26);
            }
        }
        return new string(chars);
    }

    static void Main()
    {
        int k = int.Parse(Console.ReadLine());
        string line = Console.ReadLine();
        Console.WriteLine(Shift(line, k));
    }
}
