OUTPUT_TYPE = int


def main_part_1(inp: list[str], goal: tuple[int, int] = (31, 39)) -> OUTPUT_TYPE:
    seen: set[tuple[int, int]] = set()
    to_check: list[tuple[int, tuple[int, int]]] = [(0, (1, 1))]

    while to_check:
        time: int
        active: tuple[int, int]
        time, active = to_check.pop(0)

        if active == goal:
            return time

        for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = active[0] + x_diff
            new_y = active[1] + y_diff

            if (new_x, new_y) in seen:
                continue

            if new_x < 0 or new_y < 0:
                continue

            check_sum: int = (new_x + new_y) * (new_x + new_y) + \
                3 * new_x + new_y + int(inp[0])
            if bin(check_sum).count("1") % 2:
                continue

            seen.add((new_x, new_y))
            to_check.append((time + 1, (new_x, new_y)))

    return -1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    seen: set[tuple[int, int]] = {(1, 1)}
    to_check: list[tuple[int, tuple[int, int]]] = [(0, (1, 1))]

    while to_check:
        time: int
        active: tuple[int, int]
        time, active = to_check.pop(0)

        for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = active[0] + x_diff
            new_y = active[1] + y_diff

            if (new_x, new_y) in seen:
                continue

            if new_x < 0 or new_y < 0:
                continue

            check_sum: int = (new_x + new_y) * (new_x + new_y) + \
                3 * new_x + new_y + int(inp[0])

            if bin(check_sum).count("1") % 2:
                continue

            if time + 1 > 50:
                continue

            seen.add((new_x, new_y))
            to_check.append((time + 1, (new_x, new_y)))

    return len(seen)


def main() -> None:
    test_input: str = """10"""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 11
    test_output_part_2_expected: OUTPUT_TYPE = 151

    file_location: str = "python/Advent of Code/2016/Day 13/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, (7, 4))
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
