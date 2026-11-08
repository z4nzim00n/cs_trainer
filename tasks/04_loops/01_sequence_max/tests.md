# CS_04_01. Максимум последовательности — Тесты

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

Скрипт `run_tests4_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n3 9 2 7 1` | `Max: 9\n` |
| `3\n-5 -2 -8` | `Max: -2\n` |
| `1\n42` | `Max: 42\n` |

## Автотесты

```bash
bash run_tests4_1.sh
```
