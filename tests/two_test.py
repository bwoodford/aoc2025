import pytest
from days.two import part_one, part_two


def test_part_one():
    input = []
    with open("data/two.txt", "r") as file:
        line = file.readline()
        ranges = line.split(",")

        for r in ranges:
            start_end = r.split("-")
            input.append((int(start_end[0]), int(start_end[1])))

    assert part_one(input) == 12599655151


def test_part_one_example():
    input = [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]

    assert part_one(input) == 1227775554


def test_part_two():
    input = []
    with open("data/two.txt", "r") as file:
        line = file.readline()
        ranges = line.split(",")

        for r in ranges:
            start_end = r.split("-")
            input.append((int(start_end[0]), int(start_end[1])))

    assert part_two(input) == 20942028255

def test_part_two_example():
    input = [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]

    assert part_two(input) == 4174379265


def test_part_two_1():
    input = [
        (11, 22),
    ]

    assert part_two(input) == 33

def test_part_two_2():
    input = [
        (95, 115),
    ]
    assert part_two(input) == 210


def test_part_two_3():
    input = [
        (998, 1012),
    ]
    assert part_two(input) == 2009

def test_part_two_4():
    input = [
        (1188511880, 1188511890),
    ]
    assert part_two(input) == 1188511885


def test_part_two_5():
    input = [
        (222220, 222224),
    ]
    assert part_two(input) == 222222

def test_part_two_6():
    input = [
        (1698522, 1698528),
    ]
    assert part_two(input) == 0

def test_part_two_7():
    input = [
        (446443, 446449),
    ]
    assert part_two(input) == 446446

def test_part_two_8():
    input = [
        (38593856, 38593862),
    ]
    assert part_two(input) == 38593859

def test_part_two_9():
    input = [
        (565653, 565659),
    ]
    assert part_two(input) == 565656

def test_part_two_10():
    input = [
        (824824821, 824824827),
    ]
    assert part_two(input) == 824824824

def test_part_two_11():
    input = [
        (2121212118, 2121212124),
    ]
    assert part_two(input) == 2121212121


def test_part_two_11():
    input = [
        (2121212121, 2121212121),
    ]
    assert part_two(input) == 2121212121

