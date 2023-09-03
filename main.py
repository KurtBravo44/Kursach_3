import json
from utils import func

with open("operations.json", "r", encoding="utf-8") as file:
    json_file = json.load(file)

sort_json = func.sort_file(json_file, "date")


EXECUTED_sort_json = []
# Перебираю список и удаляю пустые списки, если они есть
for i in sort_json:
    if i:
        EXECUTED_sort_json.append(i)

# Преобразую список всех транзакций в список с только выполненными операциями
for num, i in enumerate(EXECUTED_sort_json):
    if EXECUTED_sort_json[num]['state'] == 'CANCELED':
        del EXECUTED_sort_json[num]

for i in range(0, 5):
    print(func.output_of_operations(EXECUTED_sort_json, i))
    print()



