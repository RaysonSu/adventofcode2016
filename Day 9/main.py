OUTPUT_TYPE = int


def uncompress(compressed: str, recursive: bool = False) -> int:
    ret: int = 0
    while compressed:
        char = compressed[0]
        if char.isalpha():
            ret += 1
            compressed = compressed[1:]
            continue

        bracket: int = compressed.index(")")
        amount: int
        copies: int
        amount, copies = tuple(map(int, compressed[1:bracket].split("x")))

        compressed = compressed[bracket + 1:]
        copied: str = compressed[:amount]
        if recursive:
            ret += uncompress(copied, True) * copies
        else:
            ret += len(copied) * copies

        compressed = compressed[amount:]

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return uncompress(inp[0].strip())


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return uncompress(inp[0].strip(), True)


def main() -> None:
    test_input: str = """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 238
    test_output_part_2_expected: OUTPUT_TYPE = 445

    file_location: str = "python/Advent of Code/2016/Day 9/input.txt"
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
