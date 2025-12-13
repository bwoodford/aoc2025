import math


def is_even(number):
    return number % 2 == 0

def find_factors(number):
    factors = []
    limit = int(number**0.5)

    for i in range(1, limit + 1):
        if number % i == 0:
            factors.append(i)

            larger_factor = number // i

            if larger_factor != i and larger_factor != number:
                factors.append(larger_factor)

    factors.sort(reverse=True)
    return factors


def part_one(input: list[tuple]) -> int:
    total = 0

    for start, end in input:
        for num in range(start, end + 1):
            str_num = str(num)
            num_len = len(str_num)
            if num_len > 1 and is_even(num_len):
                half = num_len // 2
                if str_num[:half] == str_num[half:]:
                    total += int(str_num)

    return total


def get_pattern(factor: int, number: str):
    if factor == 1:
        return number[0]
    return number[:factor]

def part_two(input: list[tuple]) -> int:
    total = 0

    for start, end in input:
        for num in range(start, end + 1):
            str_num = str(num)
            num_len = len(str_num)
            if num_len > 1:
                factors = find_factors(num_len)
                i = 0

                while i < len(factors):
                    matches = True
                    factor = factors[i]
                    pattern = get_pattern(factor, str_num)
                    for j in range(factor, num_len, factor):
                        if pattern != str_num[j:factor+j]:
                            matches = False
                            break

                    if matches:
                        total += num
                        break

                    i += 1

    return total
