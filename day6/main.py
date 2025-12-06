#!/usr/bin/python3

from functools import reduce
from typing import Callable


def part_1() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        problemrows = []
        for row in lines:
            if row:
                problemrows.append(list(filter(lambda col: col, row.split(" "))))
        problems = zip(*problemrows)
        s = 0
        for problem in problems:
            if problem[-1] == "*":
                op = lambda x, y: x * y
                acc = 1
            else:  # problem[-1] == "+":
                op = lambda x, y: x + y
                acc = 0
            for idx in range(len(problem) - 1):
                acc = op(acc, int(problem[idx]))
            s += acc

        print(s)


def part_2() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        dividers: list[int] = [0]  # col
        for col in range(len(lines[0])):
            for row in range(len(lines)):
                if lines[row] and lines[row][col] != " ":
                    break
            else:
                dividers.append(col)
        if len(lines[0]) - 1 not in dividers:
            dividers.append(len(lines) - 1)
        chunks = list(zip(dividers, dividers[1:]))[:-1]
        chunks.append((chunks[-1][1], len(lines[0])))
        problems = []
        for start, end in chunks:
            problem = []
            for row in lines:
                if row:
                    problem.append(row[start:end])
            problem[-1] = problem[-1].strip()
            problems.append(problem)
        s = 0
        for problem in problems:
            nums: list[int] = []
            for col in range(len(problem[0])):
                curr_num = 0
                for row in range(len(problem) - 2, -1, -1):
                    n = problem[row][col]
                    if n != " ":
                        curr_num += int(n) * 10**row
                nums.append(curr_num)
            for idx, num in enumerate(nums):
                nums[idx] = int(str(num)[::-1])
            while 0 in nums:
                nums.pop(0)
            if problem[-1] == "*":
                op = lambda x, y: x * y
                acc = 1
            else:  # problem[-1] == "+":
                op = lambda x, y: x + y
                acc = 0
            for num in nums:
                acc = op(acc, num)
            s += acc

            print(nums)
        print(s)


if __name__ == "__main__":
    part_2()
