# CS_03_01. Площадь круга — Тесты

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

Скрипт `run_tests3_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `2` | `Area: 12.57\n` |
| `1` | `Area: 3.14\n` |
| `0.5` | `Area: 0.79\n` |

## Автотесты

```bash
bash run_tests3_1.sh
```
