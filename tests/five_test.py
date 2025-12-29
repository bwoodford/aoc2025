import pytest
from days.five import part_one, part_two


def test_part_one():
    input = []
    with open("data/five.txt", "r") as file:
        is_ranges = True
        ranges = []
        input = []

        for line in file.readlines():
            line = line.strip()

            if line == "":
                is_ranges = False
                continue

            if is_ranges:
                line_split = line.split("-")
                ranges.append((int(line_split[0]), int(line_split[1])))
            else:
                input.append(int(line))

    assert part_one(ranges, input) == 874


def test_part_one_example():
    ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
    input = [1, 5, 8, 11, 17, 32]
    assert part_one(ranges, input) == 3


def test_part_two():
    input = []
    with open("data/five.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()

            if line == "":
                break

            line_split = line.split("-")
            input.append((int(line_split[0]), int(line_split[1])))

    assert part_two(input) == 348548952146313


def test_part_two_example():
    input = [(3, 5), (10, 14), (16, 20), (12, 18)]
    assert part_two(input) == 14
