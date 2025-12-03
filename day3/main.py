#!/usr/bin/python3


def get_max_joltage_1(line: str) -> int:
    nums = [int(x) for x in line]

    ten = 0
    one = 0
    l = len(nums)
    for idx, num in enumerate(nums):
        if num > ten and idx < l - 1:
            ten = num
            one = nums[idx + 1]
        elif num > one:
            one = num
    return 10 * ten + one


def part_1() -> None:
    total_power = 0
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            if line:
                total_power += get_max_joltage_1(line)
    print(total_power)


def get_max_joltage_2(line: str) -> int:
    nums = [int(x) for x in line]

    out_num = [0 for _ in range(12)]
    l = len(nums)

    for i in range(l):
        # print(out_num)
        for j in range(len(out_num)):
            if nums[i] > out_num[j] and i + 12 - j < l + 1:
                out_num[j] = nums[i]
                for k in range(j + 1, 12):
                    out_num[k] = 0
                break

    s = sum(out_num[i] * 10 ** (12 - i - 1) for i in range(len(out_num)))
    print(f"{out_num} = {s}")
    return s


def part_2() -> None:
    total_power = 0
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            if line:
                total_power += get_max_joltage_2(line)
    print(total_power)


if __name__ == "__main__":
    part_2()
