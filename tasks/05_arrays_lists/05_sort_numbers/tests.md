# CS_05_05. Сортировка — Тесты

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

Скрипт `run_tests5_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n3 1 4 2 5` | `1 2 3 4 5\n` |
| `4\n10 -1 3 0` | `-1 0 3 10\n` |
| `1\n42` | `42\n` |

## Автотесты

```bash
bash run_tests5_5.sh
```
