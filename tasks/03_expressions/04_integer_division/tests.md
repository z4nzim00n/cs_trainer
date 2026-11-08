# CS_03_04. Целочисленное деление — Тесты

## Компиляция

Windows (csc из .NET Framework / Visual Studio Build Tools):

```bat
csc -nologo -langversion:latest -out:app.exe Program.cs
app.exe
```

Эталон:

```bat
csc -nologo -langversion:latest -out:app.exe Solution.cs && app.exe
csc -nologo -langversion:latest -out:app.exe SolutionCommented.cs && app.exe
```

Скрипт `run_tests3_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `7 2` | `7 / 2 = 3\n7 % 2 = 1\n` |
| `-7 2` | `-7 / 2 = -3\n-7 % 2 = -1\n` |
| `10 5` | `10 / 5 = 2\n10 % 5 = 0\n` |

## Автотесты

```bash
bash run_tests3_4.sh
```
