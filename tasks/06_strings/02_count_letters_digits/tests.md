# CS_06_02. Буквы и цифры — Тесты

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

Скрипт `run_tests6_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `abc12` | `Letters: 3\nDigits: 2\n` |
| `Hi, 2025!` | `Letters: 2\nDigits: 4\n` |
| `!!!` | `Letters: 0\nDigits: 0\n` |

## Автотесты

```bash
bash run_tests6_2.sh
```
