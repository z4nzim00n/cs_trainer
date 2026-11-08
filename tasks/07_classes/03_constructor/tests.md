# CS_07_03. Конструктор и свойства — Тесты

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

Скрипт `run_tests7_3.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `Bob 5` | `Student: Bob, Grade: 5\n` |
| `Alice 4` | `Student: Alice, Grade: 4\n` |
| `Eve 3` | `Student: Eve, Grade: 3\n` |

## Автотесты

```bash
bash run_tests7_3.sh
```
