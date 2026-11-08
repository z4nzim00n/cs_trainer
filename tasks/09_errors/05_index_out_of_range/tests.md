# CS_09_05. Выход за границы — Тесты

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

Скрипт `run_tests9_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5\n2` | `Value: 3\n` |
| `5\n1 2 3 4 5\n10` | `Error: index out of range\n` |
| `3\n1 2 3\n-1` | `Error: index out of range\n` |
| `1\n7\n0` | `Value: 7\n` |

## Автотесты

```bash
bash run_tests9_5.sh
```
