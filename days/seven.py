from collections import defaultdict


def part_one(input: list[str]) -> int:
    if len(input) == 0:
        return 0

    line_len = len(input[0])
    beams = set(i for i, val in enumerate(input[0]) if val == "S")
    total = 0

    for row in input[1:]:
        splitters = set(i for i, val in enumerate(row) if val == "^")
        # Find the beams that are being split
        intersect = beams.intersection(splitters)
        # Keep the beams that haven't been split
        difference = beams.difference(splitters)
        total += len(intersect)

        if len(intersect) == 0:
            continue

        new_beams = set()
        for split in intersect:
            if split > 0:
                new_beams.add(split - 1)
            if split < line_len - 1:
                new_beams.add(split + 1)

        beams = new_beams.union(difference)

    return total


def part_two(input: list[str]) -> int:
    if len(input) == 0:
        return 0

    s_index = next(i for i, val in enumerate(input[0]) if val == "S")
    path_dict = defaultdict(int)
    path_dict[s_index] = 1

    for i, row in enumerate(input[1:]):
        splitters = set(i for i, val in enumerate(row) if val == "^")

        if len(splitters) == 0:
            continue

        buff_dict = defaultdict(int)
        for path, timelines in path_dict.items():
            if path not in splitters:
                buff_dict[path] += timelines
            else:
                buff_dict[path - 1] += timelines
                buff_dict[path + 1] += timelines

        path_dict = buff_dict

    return sum(path_dict.values())
