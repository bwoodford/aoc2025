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
        ["*", "+", "*", "+"],
    ]

    assert part_one(input) == 4277556


def test_part_two():
    input = []
    with open("data/six.txt", "r") as file:
        for line in file.readlines():
            input.append(line.rstrip("\n"))

    assert part_two(input) == 9695042567249


def test_part_two_example():
    input = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    assert part_two(input) == 3263827


def test_part_two_fixing():
    input = [
        "27 1   527 963",
        "16 3   138 874",
        "13 29  94  759",
        "3  882 69  449",
        "*  *   *   +  ",
    ]

    assert part_two(input) == 953914146
