import pytest
from days.seven import part_one, part_two

file_loc = "data/seven.txt"


def test_part_one():
    input = []
    with open(file_loc, "r") as file:
        for line in file.readlines():
            input.append(line.strip())

    assert part_one(input) == 1533


def test_part_one_example():
    input = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    assert part_one(input) == 21


def test_part_two_example():
    input = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    assert part_two(input) == 40


def test_part_two():
    input = []
    with open(file_loc, "r") as file:
        for line in file.readlines():
            input.append(line.strip())

    assert part_two(input) == 10733529153890
