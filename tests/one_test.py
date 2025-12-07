from days.one import part_one, part_two


def test_part_one():
    input = []
    with open("data/one.txt", "r") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            input.append((direction, distance))

    assert part_one(input) == 964

def test_part_two():
    input = []
    with open("data/one.txt", "r") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            input.append((direction, distance))

    assert part_two(input) == 5872


def test_part_two_example():
    assert (
        part_two(
            [
                ("L", 68),
                ("L", 30),
                ("R", 48),
                ("L", 5),
                ("R", 60),
                ("L", 55),
                ("L", 1),
                ("L", 99),
                ("R", 14),
                ("L", 82),
            ]
        )
        == 6
    )


def test_part_two_1():
    assert part_two([("R", 49), ("L", 98)]) == 0


def test_part_two_2():
    assert part_two([("R", 49), ("R", 1)]) == 1


def test_part_two_3():
    assert part_two([("R", 49), ("R", 1), ("R", 1)]) == 1


def test_part_two_4():
    assert part_two([("R", 49), ("R", 1), ("L", 1)]) == 1


def test_part_two_5():
    assert part_two([("L", 50), ("L", 100)]) == 2


def test_part_two_6():
    assert part_two([("R", 50), ("R", 100)]) == 2


def test_part_two_7():
    assert part_two([("L", 50), ("L", 400)]) == 5


def test_part_two_8():
    assert part_two([("L", 50), ("R", 400)]) == 5


def test_part_two_9():
    assert part_two([("R", 1000)]) == 10


