# CS_13_01. Обобщённый максимум — Тесты

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

Скрипт `run_tests13_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3 7\napple banana` | `Max int: 7\nMax string: banana\n` |
| `-1 -9\ncat dog` | `Max int: -1\nMax string: dog\n` |
| `5 5\na a` | `Max int: 5\nMax string: a\n` |

## Автотесты

```bash
bash run_tests13_1.sh
```
