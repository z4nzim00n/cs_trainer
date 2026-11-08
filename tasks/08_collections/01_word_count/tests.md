# CS_08_01. Частота слов — Тесты

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

Скрипт `run_tests8_1.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `apple banana apple` | `apple: 2\nbanana: 1\n` |
| `b a b a b` | `a: 2\nb: 3\n` |
| `solo` | `solo: 1\n` |

## Автотесты

```bash
bash run_tests8_1.sh
```
