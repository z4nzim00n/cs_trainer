# CS_12_05. Поворот матрицы — Тесты

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

Скрипт `run_tests12_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `2\n1 2\n3 4` | `3 1\n4 2\n` |
| `3\n1 2 3\n4 5 6\n7 8 9` | `7 4 1\n8 5 2\n9 6 3\n` |
| `1\n7` | `7\n` |

## Автотесты

```bash
bash run_tests12_5.sh
```
