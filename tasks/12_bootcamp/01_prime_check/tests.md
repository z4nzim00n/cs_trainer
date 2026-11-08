# CS_12_01. Простое число — Тесты

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

Скрипт `run_tests12_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `7` | `True\n` |
| `9` | `False\n` |
| `1` | `False\n` |
| `2` | `True\n` |
| `13` | `True\n` |

## Автотесты

```bash
bash run_tests12_1.sh
```
