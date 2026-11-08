# CS_09_02. Разбор числа — Тесты

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

Скрипт `run_tests9_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `42` | `Number: 42\n` |
| `abc` | `Invalid number\n` |
| `-7` | `Number: -7\n` |
| `` (пустая строка) | `Invalid number\n` |

## Автотесты

```bash
bash run_tests9_2.sh
```
