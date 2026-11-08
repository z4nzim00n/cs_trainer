# CS_11_03. Счётчик с lock — Тесты

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

Скрипт `run_tests11_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `4 1000` | `Counter: 4000\n` |
| `1 5` | `Counter: 5\n` |
| `2 0` | `Counter: 0\n` |

## Автотесты

```bash
bash run_tests11_3.sh
```
