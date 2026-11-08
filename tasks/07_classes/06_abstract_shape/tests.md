# CS_07_06. Абстрактная фигура — Тесты

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

Скрипт `run_tests7_6.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `circle 2` | `Area: 12.57\n` |
| `rect 3 4` | `Area: 12.00\n` |
| `circle 1` | `Area: 3.14\n` |

## Автотесты

```bash
bash run_tests7_6.sh
```
