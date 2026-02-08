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

def part_two(input: list[str]) -> int:

    if len(input) == 0:
        return 0

    cols = len(input[0])
    rows = len(input)

    parsed_input = []
    buff_input = []

    for i in range(cols-1, -1, -1):
        buff = ""

        for j in range(rows-1):
            buff += input[j][i]

        buff = buff.replace(" ", "")

        if buff != "":
            buff_input.append(buff)

        if buff == "" or i == 0:
            parsed_input.append(buff_input)
            buff_input = []

    operations = [i for i in input[rows-1].replace(" ", "")]
    operations.reverse()

    total = 0

    for row in range(len(parsed_input)):
        col_total = int(parsed_input[row][0])
        for col in range(1, len(parsed_input[row])):
            col_total = op(operations[row], col_total, int(parsed_input[row][col]))
        total += col_total

    return total
