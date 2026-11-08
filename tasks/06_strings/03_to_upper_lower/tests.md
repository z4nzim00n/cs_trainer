# CS_06_03. Верхний и нижний регистр — Тесты

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

Скрипт `run_tests6_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `Hello World` | `UPPER: HELLO WORLD\nlower: hello world\n` |
| `C#` | `UPPER: C#\nlower: c#\n` |
| `abc` | `UPPER: ABC\nlower: abc\n` |

## Автотесты

```bash
bash run_tests6_3.sh
```
