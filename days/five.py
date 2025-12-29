import copy


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


def part_two(input: list[tuple]) -> int:
    fresh = 0
    # This unlocks the solution...doe!
    input.sort()

    c_input = copy.deepcopy(input)
    ranges = []

    while c_input:
        o_start, o_end = c_input.pop(0)

        while c_input:
            i_start, i_end = c_input[0]

            if i_start > o_end:
                break

            if o_end <= i_end and o_end >= i_start:
                o_end = i_end

            c_input.pop(0)

        ranges.append((o_start, o_end))

    for start, end in ranges:
        fresh += end - start + 1

    return fresh
