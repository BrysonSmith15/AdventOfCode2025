#!/usr/bin/python3


def part_1() -> None:
    spoiled: list[range] = []
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        divider = lines.index("")
        for lidx in range(divider):
            line = lines[lidx]
            if not line:
                continue
            sp = line.split("-")
            start = int(sp[0])
            end = int(sp[1])
            spoiled.append(range(start, end + 1))
        counter = 0
        for lidx in range(divider, len(lines)):
            if lines[lidx]:
                num = int(lines[lidx])
                for r in spoiled:
                    if num in r:
                        counter += 1
                        break
        print(counter)


def part_2() -> None:
    fresh_ranges: list[range] = []
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        divider = lines.index("")
        for lidx in range(divider):
            line = lines[lidx]
            if not line:
                continue
            sp = line.split("-")
            start = int(sp[0])
            end = int(sp[1])
            fresh_ranges.append(range(start, end + 1))
        fresh_ranges.sort(key=lambda r: r.start)
        i = 0
        while i < len(fresh_ranges) - 1:
            if fresh_ranges[i].stop > fresh_ranges[i + 1].start:
                # print(fresh_ranges[i], fresh_ranges[i + 1])
                fresh_ranges[i] = range(
                    fresh_ranges[i].start,
                    max(fresh_ranges[i + 1].stop, fresh_ranges[i].stop),
                )
                fresh_ranges.pop(i + 1)
            else:
                i += 1
        print()
        total = 0
        for r in fresh_ranges:
            print(r)
            total += r.stop - r.start
        print(total)


if __name__ == "__main__":
    part_2()
