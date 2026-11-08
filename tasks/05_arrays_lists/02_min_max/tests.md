# CS_05_02. Минимум и максимум — Тесты

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

Скрипт `run_tests5_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n4 9 1 7 3` | `Min: 1\nMax: 9\n` |
| `3\n-5 -2 -8` | `Min: -8\nMax: -2\n` |
| `1\n42` | `Min: 42\nMax: 42\n` |

## Автотесты

```bash
bash run_tests5_2.sh
```
