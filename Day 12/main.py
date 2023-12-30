OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regs: dict[str, int] = {"a": 0, "b": 0, "c": 0, "d": 0}
    instruction: int = 0

    while True:
        if instruction >= len(inp):
            return regs["a"]

        jumped: bool = False

        ins: str = inp[instruction].strip()
        chars: list[str] = ins.split(" ")

        value: int
        if chars[0] == "cpy":
            if chars[1].isnumeric():
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            regs[chars[2]] = value
        elif chars[0] == "inc":
            regs[chars[1]] += 1
        elif chars[0] == "dec":
            regs[chars[1]] -= 1
        elif chars[0] == "jnz":
            if chars[1].isnumeric():
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            if value:
                instruction += int(chars[2])
                jumped = True

        if not jumped:
            instruction += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    regs: dict[str, int] = {"a": 0, "b": 0, "c": 1, "d": 0}
    instruction: int = 0

    while True:
        if instruction >= len(inp):
            return regs["a"]

        jumped: bool = False

        ins: str = inp[instruction].strip()
        chars: list[str] = ins.split(" ")

        value: int
        if chars[0] == "cpy":
            if chars[1].isnumeric():
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            regs[chars[2]] = value
        elif chars[0] == "inc":
            regs[chars[1]] += 1
        elif chars[0] == "dec":
            regs[chars[1]] -= 1
        elif chars[0] == "jnz":
            if chars[1].isnumeric():
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            if value:
                instruction += int(chars[2])
                jumped = True

        if not jumped:
            instruction += 1


def main() -> None:
    test_input: str = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 42
    test_output_part_2_expected: OUTPUT_TYPE = 42

    file_location: str = "python/Advent of Code/2016/Day 12/input.txt"
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
