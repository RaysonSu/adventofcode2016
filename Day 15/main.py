OUTPUT_TYPE = int


def chinese_remainder(divisors: list[int], remainders: list[int]) -> int:
    if len(remainders) == 1:
        return remainders[0] % divisors[0]

    divisors = divisors.copy()
    remainders = remainders.copy()

    a_1: int = remainders.pop()
    a_2: int = remainders.pop()

    n_1: int = divisors.pop()
    n_2: int = divisors.pop()

    m_1: int
    m_2: int
    m_1, m_2 = euclidian(n_1, n_2)

    divisors.append(n_1 * n_2)
    remainders.append((a_1 * m_2 * n_2 + a_2 * m_1 * n_1) % (n_1 * n_2))

    return chinese_remainder(divisors, remainders)


def euclidian(x: int, y: int) -> tuple[int, int]:
    r_0: int = x
    r_1: int = y

    s_0: int = 1
    s_1: int = 0

    t_0: int = 0
    t_1: int = 1

    while r_1:
        quotient: int = r_0 // r_1
        r_0, r_1 = r_1, r_0 % r_1
        s_0, s_1 = s_1, s_0 - quotient * s_1
        t_0, t_1 = t_1, t_0 - quotient * t_1

    return s_0, t_0


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    rems: list[int] = []
    divs: list[int] = []
    for row in inp:
        data: list[int] = [
            int(x)
            for x in "".join([
                char.replace("x", " ")
                for char in row
                if char.isnumeric() or char in "- x"
            ]).split(" ")
            if x != ""
        ]

        rems.append(-data[3] - data[0])
        divs.append(data[1])

    return chinese_remainder(divs, rems)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    rems: list[int] = []
    divs: list[int] = []
    inp.append(f"{len(inp) + 1} 11 0 0")
    for row in inp:
        data: list[int] = [
            int(x)
            for x in "".join([
                char.replace("x", " ")
                for char in row
                if char.isnumeric() or char in "- x"
            ]).split(" ")
            if x != ""
        ]

        rems.append(-data[3] - data[0])
        divs.append(data[1])

    return chinese_remainder(divs, rems)


def main() -> None:
    test_input: str = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 5
    test_output_part_2_expected: OUTPUT_TYPE = 85

    file_location: str = "python/Advent of Code/2016/Day 15/input.txt"
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
