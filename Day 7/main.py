OUTPUT_TYPE = int


def match_abba(string: str) -> bool:
    return string[0] == string[3] and string[1] == string[2] and string[0] != string[1]


def match_aba(string: str) -> bool:
    return string[0] == string[2] and string[0] != string[1]


def match_tls(ip: str) -> bool:
    super_match: bool = False
    in_hypernet: bool = False
    seq: str = ""
    for i in ip:
        if i == "[":
            in_hypernet = True
        elif i == "]":
            in_hypernet = False

        seq += i
        if len(seq) >= 4:
            matched: bool = match_abba(seq[-4:])
            if matched:
                if in_hypernet:
                    return False
                super_match = True

    return super_match


def match_ssl(ip: str) -> bool:
    super_matches: set[str] = set()
    hyper_matches: set[str] = set()

    in_hypernet: bool = False
    seq: str = ""
    for i in ip:
        if i == "[":
            in_hypernet = True
        elif i == "]":
            in_hypernet = False

        seq += i
        if len(seq) >= 3:
            matched: bool = match_aba(seq[-3:])
            if matched:
                if in_hypernet:
                    hyper_matches.add(seq[-2:])
                else:
                    super_matches.add(seq[-2:][::-1])

    return bool(super_matches.intersection(hyper_matches))


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for ip in inp:
        if match_tls(ip):
            ret += 1

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for ip in inp:
        if match_ssl(ip):
            ret += 1

    return ret


def main() -> None:
    test_input: str = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 2
    test_output_part_2_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2016/Day 7/input.txt"
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
