import pytest
from days.three import part_one, part_two

def test_part_one():
    input = []
    with open("data/three.txt", "r") as file:
        for line in file.readlines():
            input.append(line.strip())

    assert part_one(input) == 17278


def test_part_one_example():
    input = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]

    assert part_one(input) == 357

def test_part_one_1():
    input = [
        "987654321111111",
    ]

    assert part_one(input) == 98


def test_part_one_2():
    input = [
        "811111111111119",
    ]

    assert part_one(input) == 89

def test_part_one_3():
    input = [
        "234234234234278",
    ]

    assert part_one(input) == 78

def test_part_one_4():
    input = [
        "818181911112111"
    ]

    assert part_one(input) == 92

@pytest.mark.skip()
def test_part_two():
    input = []
    with open("data/three.txt", "r") as file:
        line = file.readline()
        input.append(line.strip())

    assert part_two(input) == 0

@pytest.mark.skip()
def test_part_two_example():
    input = [
        ""
    ]

    assert part_two(input) == 0
