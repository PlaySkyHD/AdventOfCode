# Part One
def part_one(file_path):
    word = "XMAS"
    
    def check_word(x, y, visited, forwards, word_index=0):
        if word_index >= len(word):
            return True
        
        if (x, y) in visited:
            return False
            
        element_to_check = grid[y][x]
        to_check_word = word if forwards else word[::-1]
        if element_to_check != to_check_word[word_index]:
            return False
        
        visited.add((x, y))
        to_check = (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)
        for check_position in to_check:
            new_x = x + check_position[0]
            new_y = y + check_position[1]
            if new_x < 0 or new_x >= len(grid[0]):
                continue
            if new_y < 0 or new_y >= len(grid):
                continue
            if check_word(new_x, new_y, visited, forwards, word_index + 1):
                return True
        return False
    
    with open(file_path, "r") as file:
        file_content = file.read()
    grid = []
    for line in file_content.split("\n"):
        grid.append(list(line))
    start_positions = set()
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in ('X', 'S'):
                start_positions.add((x, y, grid[y][x] == "X"))
    
    count = 0
    visited = set()
    for start_position in start_positions:
        try_visited = visited.copy()
        if check_word(start_position[0], start_position[1], try_visited, start_position[2]):
            count += 1
            visited.update(try_visited)
    print(count)
    

part_one(r"2024\Day_Four\example.txt")

# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()


part_two(r"2024\Day_Four\example.txt")