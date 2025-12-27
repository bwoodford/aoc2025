def part_one(ranges: list[tuple], ingredients: list[int]) -> int:
    fresh = 0
    range_len = len(ranges)

    for ingredient in ingredients:

        i = 0
        spoiled = True

        while spoiled and i < range_len:
            start, end = ranges[i]
            if start <= ingredient <= end:
                fresh += 1
                spoiled = False
            i += 1

    return fresh


def part_two(input: list[list[str]]) -> int:
    pass
