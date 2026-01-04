import pytest
from days.six import part_one, part_two


def test_part_one():
    input = []
    with open("data/six.txt", "r") as file:
        for line in file.readlines():
            # split handles multiple spaces
            input.append(line.split())

    assert part_one(input) == 5060053676136

def test_part_one_example():
    input = [
        ["123", "328", "51", "64"],
        ["45", "64", "387", "23"],
        ["6", "98", "215", "314"],
        ["*", "+", "*", "+"]
    ]

    assert part_one(input) == 4277556


@pytest.mark.skip()
def test_part_two():
    input = []
    with open("data/six.txt", "r") as file:
        pass

    assert part_two(input) == 0

