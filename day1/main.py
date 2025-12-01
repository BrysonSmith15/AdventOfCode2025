#!/usr/bin/python3


def part_1() -> None:
    num_zeros = 0
    pos = 50
    with open("minimal_input.txt", "r") as file:
        lines = file.read().split("\n")
        print(lines)
        for line in lines:
            if line:
                pos += int(line[1:]) * (-1 if line[0] == "L" else 1)
                pos = pos % 100
            if pos == 0:
                num_zeros += 1

    print(num_zeros)


def part_2() -> None:
    num_zeros = 0
    pos = 50
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            if line:
                count = int(line[1:]) * (-1 if line[0] == "L" else 1)
                if count > 0:
                    for _ in range(count):
                        pos += 1
                        pos %= 100
                        if pos == 0:
                            num_zeros += 1
                else:
                    for _ in range(-count):
                        pos -= 1
                        pos %= 100
                        if pos == 0:
                            num_zeros += 1

    print(num_zeros)


if __name__ == "__main__":
    part_2()
