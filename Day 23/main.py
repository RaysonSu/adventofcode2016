OUTPUT_TYPE = int


def is_numeric(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError as _:
        return False


def main_part_1(inp: list[str], k: int = 7) -> OUTPUT_TYPE:
    regs: dict[str, int] = {"a": k, "b": 0, "c": 0, "d": 0}
    instruction: int = 0

    while True:
        if instruction >= len(inp):
            return regs["a"]

        jumped: bool = False

        ins: str = inp[instruction].strip()
        chars: list[str] = ins.split(" ")
#        print(regs, instruction, ins, len(inp))

        value: int
        if chars[0] == "cpy":
            if is_numeric(chars[1]):
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            if not is_numeric(chars[2]):
                regs[chars[2]] = value
        elif chars[0] == "inc":
            if not is_numeric(chars[1]):
                regs[chars[1]] += 1
        elif chars[0] == "dec":
            if not is_numeric(chars[1]):
                regs[chars[1]] -= 1
        elif chars[0] == "jnz":
            if is_numeric(chars[1]):
                value = int(chars[1])
            else:
                value = regs[chars[1]]

            if value:
                if is_numeric(chars[2]):
                    instruction += int(chars[2])
                else:
                    instruction += regs[chars[2]]
                jumped = True
        elif chars[0] == "tgl":
            if is_numeric(chars[1]):
                value = instruction + int(chars[1])
            else:
                value = instruction + regs[chars[1]]

            if value >= 0 and value < len(inp):
                inp[value] = inp[value].replace("inc", "Dec")
                inp[value] = inp[value].replace("dec", "Inc")
                inp[value] = inp[value].replace("jnz", "Cpy")
                inp[value] = inp[value].replace("cpy", "Jnz")
                inp[value] = inp[value].replace("tgl", "Inc")
                inp[value] = inp[value].lower()

        if not jumped:
            instruction += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1(inp.copy()) + 478996560


def main() -> None:
    test_input: str = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2016/Day 23/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed.copy())
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed.copy())

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file.copy())}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    print(f"Part 2: {main_part_2(input_file.copy())}")


if __name__ == "__main__":
    main()
