# CS_05_03. Разворот списка — Тесты

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

Скрипт `run_tests5_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5` | `5 4 3 2 1\n` |
| `3\n10 20 30` | `30 20 10\n` |
| `1\n7` | `7\n` |

## Автотесты

```bash
bash run_tests5_3.sh
```
