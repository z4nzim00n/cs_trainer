# CS_05_01. Сумма и среднее — Тесты

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

Скрипт `run_tests5_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5` | `Sum: 15\nAverage: 3.00\n` |
| `3\n2 4 9` | `Sum: 15\nAverage: 5.00\n` |
| `1\n7` | `Sum: 7\nAverage: 7.00\n` |

## Автотесты

```bash
bash run_tests5_1.sh
```
