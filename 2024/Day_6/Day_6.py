from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3 

def get_next_direction(direction):
    return Direction((direction.value + 1) % len(Direction))

def get_next_location(direction, x, y):
    if direction == Direction.UP:
        return (x, y - 1)
    if direction == Direction.RIGHT:
        return (x + 1, y)
    if direction == Direction.DOWN:
        return (x, y + 1)
    return (x - 1, y)

# Part One
def part_one(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    grid = [list(line) for line in file_content.split("\n")]
    
    start_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                start_pos = (x, y)
                break

    if not start_pos:
        print("Invalid Input")
        return
    
    x, y = start_pos
    current_direction = Direction.UP
    visited = {(x, y)}
    while True:
        new_x, new_y = get_next_location(current_direction, x, y)
        if new_x < 0 or new_x >= len(grid[0]):
            break
        if new_y < 0 or new_y >= len(grid):
            break
        element_to_check = grid[new_y][new_x]
        if element_to_check == "#":
            current_direction = get_next_direction(current_direction)
            continue
        visited.add((new_x, new_y))
        x, y = new_x, new_y

    print(len(visited))
part_one(r"2024\Day_6\example.txt")


# Part Two
def part_two(file_path):
    def check_loop():
        loop_x, loop_y = start_pos
        current_direction = Direction.UP
        loop_visited = {(loop_x, loop_y)}
        obstruction_hit = []
        while True:
            loop_new_x, loop_new_y = get_next_location(current_direction, loop_x, loop_y)
            if loop_new_x < 0 or loop_new_x >= len(grid[0]):
                return False
            if loop_new_y < 0 or loop_new_y >= len(grid):
                return False
            element_to_check = grid[loop_new_y][loop_new_x]
            if element_to_check == "#":
                if obstruction_hit.count((loop_new_x, loop_new_y)) > 2:
                    return True
                obstruction_hit.append((loop_new_x, loop_new_y))
                current_direction = get_next_direction(current_direction)
                continue
            loop_new_location = (loop_new_x, loop_new_y)
            loop_visited.add(loop_new_location)
            loop_x, loop_y = loop_new_location

    with open(file_path, "r") as file:
        file_content = file.read()
    grid = [list(line) for line in file_content.split("\n")]
    
    start_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                start_pos = (x, y)
                break

    if not start_pos:
        print("Invalid Input")
        return
    
    x, y = start_pos
    current_direction = Direction.UP
    visited = {(x, y)}
    path = [(x, y)]
    while True:
        new_x, new_y = get_next_location(current_direction, x, y)
        if new_x < 0 or new_x >= len(grid[0]):
            break
        if new_y < 0 or new_y >= len(grid):
            break
        element_to_check = grid[new_y][new_x]
        if element_to_check == "#":
            current_direction = get_next_direction(current_direction)
            continue
        visited.add((new_x, new_y))
        path.append((new_x, new_y))
        x, y = new_x, new_y

    directions = (-1, 0), (1, 0), (0, -1), (0, 1) 
    possible_locations = set()
    for index, path_location in enumerate(path):
        check_x, check_y = path_location
        for dx, dy in directions:
            new_x, new_y = check_x + dx, check_y + dy
            if (new_x, new_y) == start_pos:
                continue
            if new_x < 0 or new_x >= len(grid[0]):
                continue
            if new_y < 0 or new_y >= len(grid):
                continue
            if (new_x, new_y) in possible_locations:
                continue
            current_element = grid[new_y][new_x]
            if current_element == "#":
                continue
            grid[new_y][new_x] = "#"
            if check_loop():
                possible_locations.add((new_x, new_y))
            grid[new_y][new_x] = "."
        print(round(index / len(path) * 100, 2))

    print(len(possible_locations))
part_two(r"2024\Day_6\input.txt")