# CS_11_02. Два потока — Тесты

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

Скрипт `run_tests11_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `2 3` | `A: 4\nB: 9\n` |
| `-4 5` | `A: 16\nB: 25\n` |
| `0 0` | `A: 0\nB: 0\n` |

## Автотесты

```bash
bash run_tests11_2.sh
```
