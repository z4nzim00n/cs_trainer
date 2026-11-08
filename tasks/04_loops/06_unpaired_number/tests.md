# CS_04_06. Непарное число — Тесты

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

Скрипт `run_tests4_6.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n2 3 2 1 3` | `Unique: 1\n` |
| `3\n7 7 9` | `Unique: 9\n` |
| `1\n42` | `Unique: 42\n` |

## Автотесты

```bash
bash run_tests4_6.sh
```
