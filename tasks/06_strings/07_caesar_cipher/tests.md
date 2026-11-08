# CS_06_07. Шифр Цезаря — Тесты

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

Скрипт `run_tests6_7.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3\nabc xyz` | `def abc\n` |
| `1\nHello, World!` | `Ifmmp, Xpsme!\n` |
| `0\nNo change` | `No change\n` |
| `25\nab` | `za\n` |

## Автотесты

```bash
bash run_tests6_7.sh
```
