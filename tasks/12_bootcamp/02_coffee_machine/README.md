## CS_12_02. Кофейный автомат

### Задание
| CS_12_02 ||
| ------ | ------- |
| **Темы:** | состояние, команды, `if`/`else` |
| **Файл решения:** | Program.cs |
| **Входные данные:** | `n`, затем `n` команд |
| **Выходные данные** | Стандартный поток вывода (stdout) |


Автомат принимает команды:

- `water X` — добавить `X` воды;
- `coffee X` — добавить `X` кофе;
- `cup` — приготовить чашку, если есть хотя бы `200` воды и `10` кофе.

На `cup` выведи `Coffee ready` или `Not enough resources`. В конце
напечатай остатки:

~~~text
Coffee ready
Not enough resources
Water: 100
Coffee: 10
~~~

### Примеры

| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`water 500`<br>`coffee 30`<br>`cup`<br>`cup`<br>`cup` | `Coffee ready`<br>`Coffee ready`<br>`Not enough resources`<br>`Water: 100`<br>`Coffee: 10` |
| `3`<br>`water 200`<br>`coffee 10`<br>`cup` | `Coffee ready`<br>`Water: 0`<br>`Coffee: 0` |

### Как проверить

```bash
bash run_tests12_2.sh
```
