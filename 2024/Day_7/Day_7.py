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

# Part One
from itertools import product
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    available_operators = ("+", "*")
    ans = 0
    for line in file_content.split("\n"):
        line_data = line.split(": ")
        result = int(line_data[0])
        numbers = list(map(int, line_data[1].split(" ")))
        operators = list(product(available_operators, repeat=len(numbers) - 1))
        if result == 83:
            print(1)
        for operator in operators:
            if solve_function(numbers[:], list(operator)) == result:
                ans += result
                break
    print(ans)
part_one(r"2024\Day_7\input.txt")


# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
part_two(r"2024\Day_7\example.txt")