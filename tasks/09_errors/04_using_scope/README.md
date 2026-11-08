## CS_09_04. `using` и `IDisposable`

### Задание
| CS_09_04 ||
| ------ | ------- |
| **Темы:** | `IDisposable`, `using`, детерминированный порядок |
| **Файл решения:** | Program.cs |
| **Входные данные:** | Имя ресурса |
| **Выходные данные** | Стандартный поток вывода (stdout) |


Опиши класс `Resource`, который печатает `Open: имя` при создании и
`Close: имя` при освобождении. Используй `using`:

~~~text
Open: data
Use: data
Close: data
~~~

### Примеры

| Входные данные | Результат работы |
| ------ | ------ |
| `data` | `Open: data`<br>`Use: data`<br>`Close: data` |
| `log` | `Open: log`<br>`Use: log`<br>`Close: log` |

### Как проверить

```bash
bash run_tests9_4.sh
```
