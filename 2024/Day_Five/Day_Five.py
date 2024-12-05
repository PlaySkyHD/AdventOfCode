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
    middle_page_number_sum = sum([correct_order[len(correct_order) // 2] for correct_order in correct_orders])
    print(middle_page_number_sum)
part_one(r"2024\Day_Five\input.txt")

# Part Two
def part_two(file_path):
    def check_order(order):
        rule_break = None
        for index, element in enumerate(order):
            invalid_hit = False
            for rule in rules:
                if rule[0] == element:
                    if rule[1] in order[:index]:
                        rule_break = rule
                        invalid_hit = True
                        break
                if rule[1] == element:
                    if rule[0] not in order[:index + 1] and rule[0] in order:
                        rule_break = rule
                        invalid_hit = True
                        break
            if invalid_hit:
                break
        else:
            return (True, rule_break)
        return (False, rule_break)
    
    with open(file_path, "r") as file:
        file_content = file.read()
    founded_rules = re.findall(r"\d+\|\d+", file_content)
    rules = set()
    
    for rule in founded_rules:
        raw_data = rule.split("|")
        rules.add((int(raw_data[0]), int(raw_data[1])))
    orders = file_content.split("\n\n")[1]
    orders = [list(map(int, order.split(","))) for order in orders.split("\n")]
    
    in_correct_orders = []
    for order in orders:
        if not check_order(order)[0]:
            in_correct_orders.append(order)
    
    for order in in_correct_orders:
        valid, failed_rule = check_order(order)
        while not valid:
            index_one = order.index(failed_rule[0])
            index_two = order.index(failed_rule[1])
            order[index_one], order[index_two] = order[index_two], order[index_one]
            valid, failed_rule = check_order(order)
    middle_page_number_sum = sum([correct_order[len(correct_order) // 2] for correct_order in in_correct_orders])
    print(middle_page_number_sum)
part_two(r"2024\Day_Five\input.txt")