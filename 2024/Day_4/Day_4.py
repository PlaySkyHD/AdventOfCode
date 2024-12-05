# Part One
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    grid = []
    for line in file_content.split("\n"):
        grid.append(list(line))
        
    word = "XMAS"
    word_length = len(word)
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]
    
    def is_valid(x, y):
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
    
    def check_word(x, y, dx, dy):
        for i in range(word_length):
            if not is_valid(x + i * dx, y + i * dy) or grid[y + i * dy][x + i * dx] != word[i]:
                return False
        return True
    
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    count += 1
    
    print(count)
part_one(r"2024\Day_4\example.txt")

# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    grid = []
    for line in file_content.split("\n"):
        grid.append(list(line))
    patterns = [
        [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)],
        [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2)],
        [(0, 2), (1, 1), (2, 0), (0, 0), (2, 2)],
        [(0, 2), (1, 1), (2, 0), (2, 2), (0, 0)]
    ]
    
    def is_valid(x, y):
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
    
    def check_pattern(x, y, pattern):
        chars = [grid[y + dy][x + dx] for dx, dy in pattern if is_valid(x + dx, y + dy)]
        return chars in (['M', 'A', 'S', 'M', 'S'], ['S', 'A', 'M', 'S', 'M'])
    
    count = 0
    for y in range(len(grid) - 2):
        for x in range(len(grid[0]) - 2):
            for pattern in patterns:
                if check_pattern(x, y, pattern):
                    count += 1
    
    print(count // 2)

part_two(r"2024\Day_4\input.txt")