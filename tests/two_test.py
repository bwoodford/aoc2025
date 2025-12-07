from days.two import part_one, part_two


def test_part_one():
    input = []
    with open("data/two.txt", "r") as file:
        line = file.readline()
        ranges = line.split(",")

        for r in ranges:
            start_end = r.split("-")
            input.append((int(start_end[0]), int(start_end[1])))

    assert part_one(input) == 12599655151


def test_part_one_example():
    input = [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]

    assert part_one(input) == 1227775554


def test_part_two():
    input = []
    with open("data/two.txt", "r") as file:
        pass
