# CS_04_03. Максимальная цифра — Тесты

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

Скрипт `run_tests4_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `9073` | `Max digit: 9\n` |
| `0` | `Max digit: 0\n` |
| `555` | `Max digit: 5\n` |

## Автотесты

```bash
bash run_tests4_3.sh
```
