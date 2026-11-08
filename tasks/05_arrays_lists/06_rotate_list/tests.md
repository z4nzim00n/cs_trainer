# CS_05_06. Циклический сдвиг — Тесты

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

Скрипт `run_tests5_6.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `4 0\n1 2 3 4` | `1 2 3 4\n` |
| `3 5\n1 2 3` | `2 3 1\n` |

## Автотесты

```bash
bash run_tests5_6.sh
```
