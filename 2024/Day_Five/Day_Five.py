import re

# Part One
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    founded_rules = re.findall(r"\d+\|\d+", file_content)
    rules = set()
    
    for rule in founded_rules:
        raw_data = rule.split("|")
        rules.add((int(raw_data[0]), int(raw_data[1])))
    orders = file_content.split("\n\n")[1]
    orders = [list(map(int, order.split(","))) for order in orders.split("\n")]
    
    correct_orders = []
    for order in orders:
        for index, element in enumerate(order):
            invalid_hit = False
            for rule in rules:
                if rule[0] == element:
                    if rule[1] in order[:index]:
                        invalid_hit = True
                        break
                if rule[1] == element:
                    if rule[0] not in order[:index + 1] and rule[0] in order:
                        invalid_hit = True
                        break
            if invalid_hit:
                break
        else:
            correct_orders.append(order)
    ans = 0
    for correct_order in correct_orders:
        ans += correct_order[len(correct_order) // 2]
    print(ans)
part_one(r"2024\Day_Five\input.txt")

# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
part_two(r"2024\Day_Five\example.txt")