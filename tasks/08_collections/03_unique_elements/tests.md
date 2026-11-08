# CS_08_03. Уникальные элементы — Тесты

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

Скрипт `run_tests8_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n3 1 3 2 1` | `Unique: 3\n1 2 3\n` |
| `4\n7 7 7 7` | `Unique: 1\n7\n` |
| `5\n5 4 3 2 1` | `Unique: 5\n1 2 3 4 5\n` |

## Автотесты

```bash
bash run_tests8_3.sh
```
