import math


def part_one(input: list[tuple]) -> int:
    dial = 50
    password = 0
    MAX = 100

    for direction, distance in input:
        if direction == "L":
            dial = (dial - distance) % MAX
        else:
            dial = (dial + distance) % MAX

        if dial == 0:
            password += 1

    return password


def part_two(input: list[tuple]) -> int:
    dial = 50
    password = 0
    MAX = 100

    for direction, distance in input:
        is_zero = True if dial == 0 else False

        if direction == "L":
            dial = dial - distance
        else:
            dial = dial + distance

        if abs(dial) >= MAX:
            password += math.floor(abs(dial) / MAX)
        elif dial == 0:
            password += 1

        if dial < 0 and not is_zero:
            password += 1

        dial %= MAX

    return password
