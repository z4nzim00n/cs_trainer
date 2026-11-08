# CS_10_06. Статистика файла — Тесты

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

Скрипт `run_tests10_6.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `text.txt` (`hello world\nfoo\n`) | `Lines: 2\nWords: 3\nChars: 13\n` |
| `text.txt` (`one\n`) | `Lines: 1\nWords: 1\nChars: 3\n` |
| `text.txt` (пустой файл) | `Lines: 0\nWords: 0\nChars: 0\n` |

## Автотесты

```bash
bash run_tests10_6.sh
```
