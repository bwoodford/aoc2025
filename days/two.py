import math


def is_even(number):
    return number % 2 == 0


def part_one(input: list[tuple]) -> int:
    total = 0

    for start, end in input:
        for val in range(start, end + 1):
            val = str(val)
            val_len = len(val)
            if val_len > 1 and is_even(val_len):
                half = math.floor(val_len / 2)
                if val[:half] == val[half:]:
                    total += int(val)

    return total


def part_two(input: list[tuple]) -> int:
    pass
