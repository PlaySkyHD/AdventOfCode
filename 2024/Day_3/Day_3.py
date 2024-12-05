# Part One
def part_one(file_path):
    import re
    with open(file_path, "r") as file:
        file_content = file.read()
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file_content)
    ans = 0
    for instruction in instructions:
        instruction = instruction.replace("mul(", "").replace(")", "")
        data = instruction.split(",")
        ans += int(data[0]) * int(data[1])
    print(len(instructions))
part_one(r"2024\Day_3\input.txt")

# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    enabled = True
    i = 0
    ans = 0
    instructions = []
    while i < len(file_content):
        if file_content[i:].startswith("don't()"):
            enabled = False
            i += len("don't()")
            continue
        elif file_content[i:].startswith("do()"):
            enabled = True
            i += len("do()")
            continue
        if not file_content[i:].startswith("mul("):
            i += 1
            continue
        i += len("mul(")

        numbers = []
        error = False
        for y in range(2):
            number = ""
            first_number = y == 0
            for x in range(3):
                if (first_number and file_content[i + x] == ",") or (not first_number and file_content[i + x] == ")"):
                    break
                if not file_content[i + x].isdigit():
                    error = True
                    break
                number += file_content[i + x]
            
            if len(number) == 3:
                elementToCheck = file_content[i + len(number)]
                if first_number and elementToCheck != ",":
                    error = True
                elif not first_number and elementToCheck != ")":
                    error = True
            
            i += len(number) + 1
            
            if error:
                break
            
            numbers.append(number)
        if error:
            continue
        if enabled:
            instructions.append(f"mul({int(numbers[0])},{int(numbers[1])})")
            ans += int(numbers[0]) * int(numbers[1])
    print(ans)
part_two(r"2024\Day_3\example.txt")


def part_two_re(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    import re
    enabled = True
    
    i = 0
    ans = 0
    
    while i < len(file_content):
        if file_content[i:].startswith("don't()"):
            enabled = False
            i += len("don't()")
            continue
        elif file_content[i:].startswith("do()"):
            enabled = True
            i += len("do()")
            continue
        instruction_match = re.search("mul\(\d{1,3},\d{1,3}\)", file_content[i:])
        if instruction_match == None:
            i += 1
            break
        
        start_index = instruction_match.start() + i
        end_index = instruction_match.end() + i

        instruction = file_content[start_index:end_index]
        instruction = instruction.replace("mul(", "").replace(")", "")
        data = instruction.split(",")
        if enabled:
            ans += int(data[0]) * int(data[1])
        i += end_index - start_index + 1
    print(ans)
part_two_re(r"2024\Day_3\example.txt")


