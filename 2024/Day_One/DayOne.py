# Part One
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()

    x, y = [], []
    for line in file_content.split("\n"):
        line_data = line.split("   ")
        x.append(int(line_data[0]))
        y.append(int(line_data[1]))

    x.sort()
    y.sort()

    ans = 0
    for i in range(len(x)):
        diff = abs(x[i] - y[i])
        ans += diff
    
    print(ans)

part_one(r"2024\Day_One\input.txt")

# Part Two
def part_two(file_path):
    file_content = ""
    with open(file_path, "r") as file:
        file_content = file.read()

    x, y = [], []
    for line in file_content.split("\n"):
        line_data = line.split("   ")
        x.append(int(line_data[0]))
        y.append(int(line_data[1]))

    ans = 0
    for element in x:
        ans += element * y.count(element)
    print(ans)

part_two(r"2024\Day_One\input.txt")