# Part One
from itertools import product
def part_one(file_path):
    def solve_function(numbers: list, operators: list) -> int:
        if len(numbers) == 1:
            return numbers[0]
        base_number = numbers.pop(0)
        for _ in range(len(numbers)):
            operator = operators.pop(0)
            number = numbers.pop(0)
            if operator == "*":
                base_number *= number
            else:
                base_number += number
        return base_number
    
    with open(file_path, "r") as file:
        file_content = file.read()
    available_operators = ("+", "*")
    ans = 0
    for line in file_content.split("\n"):
        line_data = line.split(": ")
        result = int(line_data[0])
        numbers = list(map(int, line_data[1].split(" ")))
        operators = list(product(available_operators, repeat=len(numbers) - 1))
        for operator_pattern in operators:
            if solve_function(numbers[:], list(operator_pattern)) == result:
                ans += result
                break
    print(ans)
part_one(r"2024\Day_7\input.txt")


# Part Two
def part_two(file_path):
    def solve_function(numbers: list, operators: list) -> int:
        if len(numbers) == 1:
            return numbers[0]
        current_number = numbers.pop(0)
        while numbers:
            operator = operators.pop(0)
            number = numbers.pop(0)
            if operator == "*":
                current_number *= number
            elif operator == "+":
                current_number += number
            else:
                current_number = int(str(current_number) + str(number))
        return current_number
    
    with open(file_path, "r") as file:
        file_content = file.read()
    available_operators = ("+", "*", "||")
    ans = 0
    lines = file_content.split("\n")
    for index, line in enumerate(lines):
        line_data = line.split(": ")
        result = int(line_data[0])
        numbers = list(map(int, line_data[1].split(" ")))
        operators = list(product(available_operators, repeat=len(numbers) - 1))
        for operator_pattern in operators:
            if solve_function(numbers[:], list(operator_pattern)) == result:
                 ans += result
                 break
        print(round(index / len(lines) * 100, 2),"%")
    print(ans)
part_two(r"2024\Day_7\input.txt")