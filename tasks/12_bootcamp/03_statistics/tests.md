# CS_12_03. Статистика — Тесты

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

Скрипт `run_tests12_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5` | `Min: 1\nMax: 5\nSum: 15\nAverage: 3.00\n` |
| `3\n2 4 9` | `Min: 2\nMax: 9\nSum: 15\nAverage: 5.00\n` |
| `1\n-5` | `Min: -5\nMax: -5\nSum: -5\nAverage: -5.00\n` |

## Автотесты

```bash
bash run_tests12_3.sh
```
