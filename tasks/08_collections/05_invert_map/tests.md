# CS_08_05. Инверсия словаря — Тесты

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

Скрипт `run_tests8_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3\na 1\nb 2\nc 3` | `1: a\n2: b\n3: c\n` |
| `2\nx 10\ny 5` | `5: y\n10: x\n` |
| `1\nonly 42` | `42: only\n` |

## Автотесты

```bash
bash run_tests8_5.sh
```
