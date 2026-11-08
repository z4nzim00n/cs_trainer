# CS_12_02. Кофейный автомат — Тесты

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

Скрипт `run_tests12_2.sh` сам находит `csc.exe` и собирает выбранный файл.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\nwater 500\ncoffee 30\ncup\ncup\ncup` | `Coffee ready\nCoffee ready\nNot enough resources\nWater: 100\nCoffee: 10\n` |
| `3\nwater 200\ncoffee 10\ncup` | `Coffee ready\nWater: 0\nCoffee: 0\n` |
| `4\nwater 199\ncoffee 10\ncup\ncup` | `Not enough resources\nNot enough resources\nWater: 199\nCoffee: 10\n` |

## Автотесты

```bash
bash run_tests12_2.sh
```
