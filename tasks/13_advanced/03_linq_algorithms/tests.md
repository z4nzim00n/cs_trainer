# CS_13_03. LINQ — Тесты

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

Скрипт `run_tests13_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `6\n1 2 3 4 5 6` | `Sum: 56\n` |
| `3\n1 3 5` | `Sum: 0\n` |
| `4\n-2 -1 0 2` | `Sum: 8\n` |

## Автотесты

```bash
bash run_tests13_3.sh
```
