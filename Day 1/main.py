OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> int:
    position: list[int] = [0, 0]
    direction: int = 1

    for instruction in inp[0].strip().split(", "):
        new_dir: str = instruction[0]
        amount: int = int(instruction[1:])

        direction += {"L": 1, "R": -1}[new_dir]
        position[0] += [1, 0, -1, 0][direction % 4] * amount
        position[1] += [0, -1, 0, 1][direction % 4] * amount

    return sum(map(abs, position))


def main_part_2(inp: list[str]) -> int:
    position: list[int] = [0, 0]
    seen: set[tuple[int, int]] = set()
    direction: int = 1

    for instruction in inp[0].strip().split(", "):
        new_dir: str = instruction[0]
        amount: int = int(instruction[1:])

        direction += {"L": 1, "R": -1}[new_dir]
        for _ in range(amount):
            if tuple(position) in seen:
                return sum(map(abs, position))

            seen.add((position[0], position[1]))

            position[0] += [1, 0, -1, 0][direction % 4]
            position[1] += [0, -1, 0, 1][direction % 4]

    return sum(map(abs, position))


def main() -> None:
    test_input: str = """R8, R4, R4, R8"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 8
    test_output_part_2_expected: OUTPUT_TYPE = 4

    file_location: str = "python/Advent of Code/2016/Day 1/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
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
