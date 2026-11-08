# CS_10_03. Копирование файла — Тесты

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

Скрипт `run_tests10_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `input.txt\ncopy.txt` | `Copied: copy.txt\n`, файл `abc\n` |
| повторное копирование поверх старого | файл заменён |

## Автотесты

```bash
bash run_tests10_3.sh
```
