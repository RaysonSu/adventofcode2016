def main_part_1(inp: list[str]) -> int:
    return int(bin(int(inp[0]))[3:] + "1", 2)


def main_part_2(inp: list[str]) -> int:
    elves: int = int(inp[0])

    a: int = 2
    b: int = 2
    c: int = 4

    while c <= elves:
        a, b, c = c, 3 * b, 3 * c - 2

    if elves < b:
        return elves - a + 1
    else:
        return (b - a) + 2 * (elves - b) + 1


def main() -> None:
    test_input: str = """5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: int = 3
    test_output_part_2_expected: int = 2

    file_location: str = "python/Advent of Code/2016/Day 19/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: int = main_part_1(test_input_parsed)
    test_output_part_2: int = main_part_2(test_input_parsed)

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
