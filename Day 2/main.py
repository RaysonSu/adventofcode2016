OUTPUT_TYPE = str


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[str] = [
        "     ",
        " 123 ",
        " 456 ",
        " 789 ",
        "     "
    ]

    ret: str = ""
    position: list[int] = [2, 2]
    for row in inp:
        for direc in row.strip():
            pos_backup = position.copy()
            if direc == "U":
                position[1] -= 1
            elif direc == "D":
                position[1] += 1
            elif direc == "L":
                position[0] -= 1
            elif direc == "R":
                position[0] += 1

            if grid[position[1]][position[0]] == " ":
                position = pos_backup

        ret += grid[position[1]][position[0]]

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[str] = [
        "       ",
        "   1   ",
        "  234  ",
        " 56789 ",
        "  ABC  ",
        "   D   ",
        "       "
    ]

    ret: str = ""
    position: list[int] = [1, 3]
    for row in inp:
        for direc in row.strip():
            pos_backup = position.copy()
            if direc == "U":
                position[1] -= 1
            elif direc == "D":
                position[1] += 1
            elif direc == "L":
                position[0] -= 1
            elif direc == "R":
                position[0] += 1

            if grid[position[1]][position[0]] == " ":
                position = pos_backup

        ret += grid[position[1]][position[0]]

    return ret


def main() -> None:
    test_input: str = """ULL
RRDDD
LURDL
UUUUD"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "1985"
    test_output_part_2_expected: OUTPUT_TYPE = "5DB3"

    file_location: str = "python/Advent of Code/2016/Day 2/input.txt"
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
