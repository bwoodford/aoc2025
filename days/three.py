def part_one(input: list[str]) -> int:
    total = 0

    for bank in input:
        max_1 = 0
        max_2 = 0
        bank_len = len(bank)

        for i, batt_jolt in enumerate(bank):
            joltage = int(batt_jolt)
            if joltage > max_1:
                if i == bank_len - 1:
                    max_2 = joltage
                else:
                    max_1 = joltage
                    max_2 = 0
                continue

            if joltage > max_2:
                max_2 = joltage

        total += int(f"{max_1}{max_2}")

    return total


def find_max(bank: str, start: int, end: int) -> tuple[str, int]:
    curr_max = (0, 0)

    for i, battery in enumerate(bank[start:end]):
        joltage = int(battery)
        if joltage > curr_max[0]:
            curr_max = (joltage, start + i)

    return (str(curr_max[0]), curr_max[1])


def part_two(input: list[str]) -> int:
    banks = []
    MAX_BANK_LEN = 12
    for bank in input:
        ans_bank = ""
        total_banks = 0
        bank_len = len(bank)
        index = 0

        while total_banks < MAX_BANK_LEN:
            # +1 to include the 12th from the last character in the comparison
            joltage, index = find_max(
                bank, index, bank_len - (MAX_BANK_LEN - total_banks) + 1
            )
            ans_bank += joltage
            total_banks += 1
            index += 1

        banks.append(int(ans_bank))

    return sum(banks)
