#!/usr/bin/python3


def part_1() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        i = 0
        while i < len(lines):
            # if "^" not in lines[i] and "S" not in lines[i]:
            #     lines.pop(i)
            if not lines[i]:
                lines.pop(i)
            else:
                i += 1
        for line in lines:
            print(line)

        cols: set[int] = set([lines[0].index("S")])
        splits = 0
        for idx, row in enumerate(lines):
            print()
            new_cols: set[int] = set()
            split_cols: list[int] = []
            for col in cols:
                if row[col] == "^":
                    splits += 1
                    split_cols.append(col)
                    new_cols.add(col - 1)
                    new_cols.add(col + 1)
                else:
                    new_cols.add(col)
            cols = new_cols
            for col in cols:
                lines[idx] = lines[idx][:col] + "|" + lines[idx][col + 1 :]
            for col in split_cols:
                lines[idx] = lines[idx][:col] + "@" + lines[idx][col + 1 :]
            print(splits)
            for line in lines:
                print(line)
        print(splits)


def simulate_timeline(
    grid: list[str], row: int, col: int, results: dict[tuple[int, int], int] = {}
) -> int:
    if (row, col) in results:
        return results[(row, col)]
    if row == len(grid):
        return 0
    while grid[row][col] != "^":
        row += 1
        if row == len(grid):
            return 0
    a = (
        1
        + simulate_timeline(grid, row + 1, col - 1)
        + simulate_timeline(grid, row + 1, col + 1)
    )
    results[(row, col)] = a
    return a


def part_2() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        i = 0
        while i < len(lines):
            if not lines[i] or ("S" not in lines[i] and "^" not in lines[i]):
                lines.pop(i)
            else:
                i += 1

        for line in lines:
            print(line)

        print(len(lines[0]))
        print(simulate_timeline(lines, 0, lines[0].index("S")) + 1)


if __name__ == "__main__":
    part_2()
