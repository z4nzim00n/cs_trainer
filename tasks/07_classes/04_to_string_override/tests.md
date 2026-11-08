# CS_07_04. Переопределение ToString — Тесты

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

Скрипт `run_tests7_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `1 2` | `Point(1, 2)\n` |
| `-3 7` | `Point(-3, 7)\n` |
| `0 0` | `Point(0, 0)\n` |

## Автотесты

```bash
bash run_tests7_4.sh
```
