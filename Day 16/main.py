OUTPUT_TYPE = str


def iterate(curve: str) -> str:
    return curve + "0" + curve[::-1].replace("0", "2").replace("1", "0").replace("2", "1")


def checksum_reduce(curve: str) -> str:
    return "".join(map(lambda x, y: "1" if x == y else "0", curve[::2], curve[1::2]))


def main_part_1(inp: list[str], length: int = 272) -> OUTPUT_TYPE:
    curve: str = inp[0].strip()
    while len(curve) < length:
        curve = iterate(curve)
    curve = curve[:length]

    while len(curve) % 2 == 0:
        curve = checksum_reduce(curve)

    return curve


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1(inp, 35651584)


def main() -> None:
    test_input: str = """10000"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "01100"

    file_location: str = "python/Advent of Code/2016/Day 16/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 20)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
