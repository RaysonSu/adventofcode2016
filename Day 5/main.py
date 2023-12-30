from hashlib import md5 as md
OUTPUT_TYPE = str


def md5(x: str) -> str:
    return md(x.encode()).hexdigest().zfill(32)


def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]


def str_format(string: str, chars: int, replacement: str) -> str:
    return string[:chars] + replacement * max(0, chars - len(string))


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: str = ""
    key: str = inp[0].strip()

    guess: int = 0
    while len(ret) < 8:
        hashed: str = md5(key + str(guess))
        if hashed.startswith("00000"):
            ret += hashed[5]
            # print(f"\rFound: {key}{guess} {hashed}")

        # print("\r" + str_format(ret, 8, "_"), f"{key}{guess}", hashed, end="")
        guess += 1

    # print(f"\rFinal password to key {key}: {ret}                          \n")

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: str = "________"
    key: str = inp[0].strip()

    guess: int = 0
    while "_" in ret:
        hashed: str = md5(key + str(guess))

        if hashed.startswith("00000"):
            sixth: int = int(hashed[5], 16)
            if sixth < len(ret) and ret[sixth] == "_":
                ret = str_assign(ret, sixth, hashed[6])
                # print(f"\rFound: {key}{guess} {hashed}")

        # print("\r" + str_format(ret, 8, "_"), f"{key}{guess}", hashed, end="")
        guess += 1

    # print(f"\rFinal password to key {key}: {ret}                          \n")

    return ret


def main() -> None:
    test_input: str = """abc"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = "18f47a30"
    test_output_part_2_expected: OUTPUT_TYPE = "05ace8e3"

    file_location: str = "python/Advent of Code/2016/Day 5/input.txt"
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
