OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row in inp:
        sides: list[int] = [int(c) for c in row.split(" ") if c.isnumeric()]
        if sum(sides) > 2 * max(sides):
            ret += 1
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row_index in range(len(inp) // 3):
        triangles: list[list[int]] = [[], [], []]
        for i in range(3):
            sides: list[int] = [
                int(c) for c in inp[row_index * 3 + i].split(" ") if c.isnumeric()]
            for j, amt in enumerate(sides):
                triangles[j].append(amt)
        for sides in triangles:
            if sum(sides) > 2 * max(sides):
                ret += 1
    return ret


def main() -> None:
    test_input: str = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 3
    test_output_part_2_expected: OUTPUT_TYPE = 6

    file_location: str = "python/Advent of Code/2016/Day 3/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
