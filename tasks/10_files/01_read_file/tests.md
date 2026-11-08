# CS_10_01. Чтение файла — Тесты

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

Скрипт `run_tests10_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `input.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `input.txt` (`abc`, без `\n`) | `abc` |
| `missing.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_1.sh
```
