MAX_ROLLS = 3
PAPER = "@"


def adj_check(
    input: list[list[str]], x: int, y: int, len_rows: int, len_cols: int
) -> int:
    adj_rolls = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            # Skip the current item we're testing from
            if dr == 0 and dc == 0:
                continue

            nr = y + dr
            nc = x + dc

            # The 0 equality checks are used to keep us from counting
            # the current element.
            if not (0 <= nr < len_rows and 0 <= nc < len_cols):
                continue

            if input[nr][nc] == PAPER:
                adj_rolls += 1

    return adj_rolls


def part_one(input: list[list[str]]) -> int:
    accessed = 0
    len_rows = len(input)
    len_cols = len(input[0])

    for y in range(len_rows):
        for x in range(len_cols):
            if input[y][x] != PAPER:
                continue

            adj_rolls = adj_check(input, x, y, len_rows, len_cols)

            if adj_rolls <= MAX_ROLLS:
                accessed += 1

    return accessed


def part_two(input: list[list[str]]) -> int:
    len_rows = len(input)
    len_cols = len(input[0])

    total = 0
    prev_total = -1

    while prev_total != total:
        prev_total = total
        roll_points = []
        for y in range(len_rows):
            for x in range(len_cols):
                if input[y][x] != PAPER:
                    continue

                adj_rolls = adj_check(input, x, y, len_rows, len_cols)

                if adj_rolls <= MAX_ROLLS:
                    total += 1
                    roll_points.append((x, y))

        for point in roll_points:
            x, y = point
            input[y][x] = "."

    return total
