
def part_one(input: list[str]) -> int:
    total = 0

    for bank in input:
        max_1 = 0
        max_2 = 0
        bank_len = len(bank)

        for i, batt_jolt in enumerate(bank):
            joltage = int(batt_jolt)
            if joltage > max_1:
                if i == bank_len-1:
                    max_2 = joltage
                else:
                    max_1 = joltage
                    max_2 = 0
                continue

            if joltage > max_2:
                max_2 = joltage

        total += int(f"{max_1}{max_2}")

    return total

def part_two(input: list[str]) -> int:
    pass
