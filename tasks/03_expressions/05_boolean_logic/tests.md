# CS_03_05. Логическое выражение — Тесты

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

Скрипт `run_tests3_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `20 1` | `Allowed: True\n` |
| `17 1` | `Allowed: False\n` |
| `20 0` | `Allowed: False\n` |
| `18 1` | `Allowed: True\n` |

## Автотесты

```bash
bash run_tests3_5.sh
```
