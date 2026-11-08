# CS_11_05. Параллельная сумма — Тесты

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

Скрипт `run_tests11_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5` | `Sum: 15\n` |
| `4\n-1 10 -2 3` | `Sum: 10\n` |
| `1\n7` | `Sum: 7\n` |
| `0\n` | `Sum: 0\n` |

## Автотесты

```bash
bash run_tests11_5.sh
```
