from collections import defaultdict
OUTPUT_TYPE = str


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    counts: list[defaultdict[str, int]] = [
        defaultdict(lambda: 0)
        for _ in inp[0]
    ]

    for row in inp:
        for index, char in enumerate(row):
            counts[index][char] += 1

    ret: str = ""
    for count in counts:
        view: list[tuple[str, int]] = list(count.items())
        view.sort(key=lambda x: x[1], reverse=True)

        ret += view[0][0]

    return ret.strip()


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    counts: list[defaultdict[str, int]] = [
        defaultdict(lambda: 0)
        for _ in inp[0]
    ]

    for row in inp:
        for index, char in enumerate(row):
            counts[index][char] += 1

    ret: str = ""
    for count in counts:
        view: list[tuple[str, int]] = list(count.items())
        view.sort(key=lambda x: x[1], reverse=False)

        ret += view[0][0]

    return ret.strip()


def main() -> None:
    test_input: str = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "easter"
    test_output_part_2_expected: OUTPUT_TYPE = "advent"

    file_location: str = "python/Advent of Code/2016/Day 6/input.txt"
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
