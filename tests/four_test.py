import pytest
from days.four import part_one, part_two


def test_part_one():
    input = []
    with open("data/four.txt", "r") as file:
        for line in file.readlines():
            row = []
            positions = line.strip()
            for position in positions:
                row.append(position)
            input.append(row)
    assert part_one(input) == 1495


def test_part_one_example():
    input = [
        [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
        ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
        ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
        ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
        ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
    ]
    assert part_one(input) == 13


@pytest.mark.skip()
def test_part_two():
    input = []
    with open("data/four.txt", "r") as file:
        for line in file.readlines():
            row = []
            positions = line.strip()
            for position in positions:
                row.append(position)
            input.append(row)
    assert part_two(input) == 0


@pytest.mark.skip()
def test_part_two_example():
    input = [
        [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
        ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
        ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
        ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
        ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
    ]
    assert part_two(input) == 0
