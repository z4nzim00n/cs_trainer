# CS_12_04. Гистограмма — Тесты

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

Скрипт `run_tests12_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n2 5 2 2 5` | `2: ***\n5: **\n` |
| `3\n0 9 0` | `0: **\n9: *\n` |
| `1\n7` | `7: *\n` |

## Автотесты

```bash
bash run_tests12_4.sh
```
