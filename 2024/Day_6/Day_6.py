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
part_one(r"2024\Day_6\input.txt")

# Part Two
def part_two(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
part_two(r"2024\Day_6\input.txt")