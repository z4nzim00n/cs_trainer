# CS_10_05. Слова в файле — Тесты

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

Скрипт `run_tests10_5.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `text.txt` (`hello world\nfoo\n`) | `Words: 3\n` |
| `text.txt` (`  one   two  `) | `Words: 2\n` |
| `text.txt` (пустой файл) | `Words: 0\n` |

## Автотесты

```bash
bash run_tests10_5.sh
```
