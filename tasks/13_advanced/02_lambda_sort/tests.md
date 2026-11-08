# CS_13_02. Сортировка лямбдой — Тесты

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

Скрипт `run_tests13_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `4\nbbb a cc ab` | `a ab cc bbb\n` |
| `3\nbb aa c` | `c aa bb\n` |
| `2\nsame same` | `same same\n` |

## Автотесты

```bash
bash run_tests13_2.sh
```
