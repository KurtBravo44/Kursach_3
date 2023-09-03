import json
from utils import func

with open("operations.json", "r", encoding="utf-8") as file:
    json_file = json.load(file)

sort_json_file = func.sort_file(json_file, "date")


for i in range(0, 5):
    print(func.output_of_operations(sort_json_file, i))
    print()



