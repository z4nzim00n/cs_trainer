# CS_02_02. Сумма двух чисел — Тесты

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

Скрипт `run_tests2_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `2 3` | `Sum: 5\n` |
| `-4 4` | `Sum: 0\n` |
| `100 200` | `Sum: 300\n` |

## Автотесты

```bash
bash run_tests2_2.sh
```
