# CS_08_02. Поиск в словаре — Тесты

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

Скрипт `run_tests8_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3\napple 5\nbanana 7\nkiwi 3\nbanana` | `Found: 7\n` |
| `2\na 1\nb 2\nz` | `Not found\n` |
| `0\nkey` | `Not found\n` |

## Автотесты

```bash
bash run_tests8_2.sh
```
