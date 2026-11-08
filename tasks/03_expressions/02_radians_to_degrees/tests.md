# CS_03_02. Радианы в градусы — Тесты

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

Скрипт `run_tests3_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3.14159265358979` | `Degrees: 180.00\n` |
| `1.5707963267949` | `Degrees: 90.00\n` |
| `0` | `Degrees: 0.00\n` |

## Автотесты

```bash
bash run_tests3_2.sh
```
