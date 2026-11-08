# CS_05_04. Убрать дубликаты — Тесты

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

Скрипт `run_tests5_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `7\n1 2 1 3 2 4 1` | `1 2 3 4\n` |
| `4\n5 5 5 5` | `5\n` |
| `3\n3 2 1` | `3 2 1\n` |

## Автотесты

```bash
bash run_tests5_4.sh
```
