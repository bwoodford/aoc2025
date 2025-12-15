def part_one(input: list[list[str]]) -> int:
    MAX_ROLLS = 3
    PAPER = "@"
    accessed = 0
    len_rows = len(input)
    len_cols = len(input[0])

    for i in range(len_rows):
        for j in range(len_cols):
            if input[i][j] != PAPER:
                continue

            adj_rolls = 0

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    # Skip the current item we're testing from
                    if dr == 0 and dc == 0:
                        continue

                    nr = i + dr
                    nc = j + dc

                    # The 0 equality checks are used to keep us from counting
                    # the current element.
                    if not (0 <= nr < len_rows and 0 <= nc < len_cols):
                        continue

                    if input[nr][nc] == PAPER:
                        adj_rolls += 1

            if adj_rolls <= MAX_ROLLS:
                accessed += 1

    return accessed


def part_two(input: list[list[str]]) -> int:
    pass
