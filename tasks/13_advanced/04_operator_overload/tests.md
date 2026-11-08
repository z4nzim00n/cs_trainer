# CS_13_04. Перегрузка оператора — Тесты

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

Скрипт `run_tests13_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `1 2 3 4` | `(4, 6)\n` |
| `-1 5 1 -5` | `(0, 0)\n` |
| `0 0 0 0` | `(0, 0)\n` |

## Автотесты

```bash
bash run_tests13_4.sh
```
