# CS_10_02. Запись файла — Тесты

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

Скрипт `run_tests10_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `output.txt\nhello` | `Written: output.txt\n`, файл `hello` |
| `text.txt\nhello world` | `Written: text.txt\n`, файл `hello world` |

## Автотесты

```bash
bash run_tests10_2.sh
```
