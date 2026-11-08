# CS_02_04. Форматирование числа — Тесты

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

Скрипт `run_tests2_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3.14159` | `Value: 3.14\n` |
| `2` | `Value: 2.00\n` |
| `0.5` | `Value: 0.50\n` |

## Автотесты

```bash
bash run_tests2_4.sh
```
