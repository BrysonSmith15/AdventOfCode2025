#!/usr/bin/python3
from itertools import repeat


def is_duplicates(num: str) -> bool:
    return num == "".join(repeat(num[: len(num) // 2], 2))


def is_duplicates2(num: str) -> bool:
    return num == "".join(repeat(num[: len(num) // 2], 2))


def part_1() -> None:
    count = 0
    with open("input.txt", "r") as file:
        ranges = file.read().split(",")
        for m_range in ranges:
            m = m_range.split("-")
            i = int(m[0])
            j = int(m[1])
            for k in range(i, j + 1):
                if is_duplicates(str(k)):
                    count += k
    print()
    print(count)


if __name__ == "__main__":
    part_1()
    # print(is_duplicates("446446"))
    # print(is_duplicates("55"))
    # print(is_duplicates("123"))
    # print(is_duplicates("123123"))
