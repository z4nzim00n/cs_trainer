# CS_08_04. Группировка по длине — Тесты

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

Скрипт `run_tests8_4.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `dog elephant cat sun` | `3: cat dog sun\n8: elephant\n` |
| `aa b ccc` | `1: b\n2: aa\n3: ccc\n` |
| `one two` | `3: one two\n` |

## Автотесты

```bash
bash run_tests8_4.sh
```
