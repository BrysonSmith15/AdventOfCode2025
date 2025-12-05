#!/usr/bin/python3


def get_num_neighbors(
    grid: list[list[bool]], row: int, col: int, used: set[tuple[int, int]] = set()
) -> int:
    dirs = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]
    s = 0
    for r, c in dirs:
        if (row, col) not in used:
            if (
                0 <= row + r
                and row + r < len(grid)
                and 0 <= col + c
                and col + c < len(grid[row + r])
            ):
                if grid[row + r][col + c]:
                    # print(row, col, grid[row + r][col + c])
                    s += 1
    if s < 4:
        used.add((row, col))
    # print(sorted(list(used), key=lambda location: location[0]))

    return s


def part_1() -> None:
    with open("input.txt", "r") as file:
        grid = [[col == "@" for col in row] for row in file.read().split("\n")]
        for row in grid:
            if row:
                print(row)
        accessible = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    accessible += 1 if get_num_neighbors(grid, row, col) < 4 else 0
        print(accessible)
        # print(get_num_neighbors(grid, 0, 7))


def part_2() -> None:
    with open("input.txt", "r") as file:
        grid = [[col == "@" for col in row] for row in file.read().split("\n")]
        for row in grid:
            if row:
                print(row)
        total = 0
        while True:
            accessible: list[tuple[int, int]] = []
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] and get_num_neighbors(grid, row, col) < 4:
                        accessible.append((row, col))
            for ridx, row in enumerate(grid):
                for cidx, col in enumerate(row):
                    if (ridx, cidx) in accessible:
                        print("x", end="")
                    elif grid[ridx][cidx]:
                        print("@", end="")
                    else:
                        print(".", end="")
                print()
            for row, col in accessible:
                grid[row][col] = False
            if len(accessible) == 0:
                print(total)
                exit()
            total += len(accessible)


if __name__ == "__main__":
    part_2()
