# Part One
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    reports = file_content.split("\n")
    unsafe = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        descending = None
        for i in range(1, len(levels)):
            if descending == None:
                descending = levels[i - 1] > levels[i]
            if (descending and levels[i - 1] < levels[i]) or (not descending and levels[i - 1] > levels[i]):
                unsafe += 1
                break
            
            diff = abs(levels[i] - levels[i - 1])
            if diff not in (1, 2, 3):
                unsafe += 1
                break
    print(f"Safe: {len(reports) - unsafe}")
    print(f"Unsafe: {unsafe}")
part_one(r"2024\Day_Two\input.txt")

# Part Two
def part_two(file_path):
    def check_report(levels):
        descending = None
        for i in range(1, len(levels)):
            if descending == None:
                descending = levels[i - 1] > levels[i]
            if (descending and levels[i - 1] < levels[i]) or (not descending and levels[i - 1] > levels[i]):
                return False
            
            diff = abs(levels[i] - levels[i - 1])
            if diff not in (1, 2, 3):
                return False
        return True
            
    with open(file_path, "r") as file:
        file_content = file.read()
    reports = file_content.split("\n")
    
    unsafe = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        is_valid = check_report(levels)
        if is_valid:
            continue
        valid = False
        for i in range(len(levels)):
            with_out_index = levels[:]
            with_out_index.pop(i)
            is_valid = check_report(with_out_index)
            if is_valid:
                valid = True
                break
        if not valid:
            unsafe += 1
    
    print(f"Safe: {len(reports) - unsafe}")
    print(f"Unsafe: {unsafe}")

part_two(r"2024\Day_Two\input.txt")