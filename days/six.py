def op(operation: str, a: int, b: int) -> int:
    if operation == "*":
        return a * b
    return a + b

def part_one(input: list[list[str]]) -> int:
    cols = len(input[0])
    rows = len(input)
    total = 0

    for col in range(cols):
        row_total = int(input[0][col])
        for row in range(1, rows-1):
            row_total = op(input[-1][col], row_total, int(input[row][col]))
        total += row_total
    return total

def part_two(input) -> int:
    pass
