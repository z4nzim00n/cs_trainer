# CS_09_01. Безопасное деление — Тесты

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

Скрипт `run_tests9_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `10 2` | `Result: 5\n` |
| `7 0` | `Error: division by zero\n` |
| `-7 2` | `Result: -3\n` |

## Автотесты

```bash
bash run_tests9_1.sh
```
