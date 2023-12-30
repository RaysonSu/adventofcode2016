from itertools import permutations
OUTPUT_TYPE = str


def rotate_list(data: list[str], amount: int) -> list[str]:
    amount %= len(data)
    return data[-amount:] + data[:-amount]


def swap_pos(data: list[str], start: int, end: int) -> list[str]:
    new_data: list[str] = data.copy()
    new_data[start], new_data[end] = new_data[end], new_data[start]
    return new_data


def swap_char(data: list[str], char_1: str, char_2: str) -> list[str]:
    return swap_pos(data, data.index(char_1), data.index(char_2))


def move_char(data: list[str], start: int, end: int) -> list[str]:
    new_data: list[str] = data.copy()
    new_data.insert(end, new_data.pop(start))
    return new_data


def rev(data: list[str], start: int, end: int) -> list[str]:
    a = data[:start]
    if start == 0:
        b = data[end::-1]
    else:
        b = data[end:start - 1:-1]
    c = data[end + 1:]
    return a + b + c


def main_part_1(inp: list[str], initial: str = "abcdefgh") -> OUTPUT_TYPE:
    data: list[str] = list(initial)
    for instruction in inp:
        parsed: list[str] = instruction.strip().split(" ")
        if parsed[0] == "swap":
            if parsed[1] == "position":
                data = swap_pos(data, int(parsed[2]), int(parsed[5]))
            else:
                data = swap_char(data, parsed[2], parsed[5])
        elif parsed[0] == "reverse":
            data = rev(data, int(parsed[2]), int(parsed[4]))
        elif parsed[0] == "move":
            data = move_char(data, int(parsed[2]), int(parsed[5]))
        elif parsed[0] == "rotate":
            if parsed[1] == "left":
                data = rotate_list(data, -int(parsed[2]))
            elif parsed[1] == "right":
                data = rotate_list(data, int(parsed[2]))
            else:
                amount: int = data.index(parsed[6])
                if amount >= 4:
                    amount += 1
                amount += 1

                data = rotate_list(data, amount)

    return "".join(data)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    for permute in permutations("abcdefgh"):
        guess: str = "".join(permute)
        if main_part_1(inp, guess) == "fbgdceah":
            return guess

    return ""


def main() -> None:
    test_input: str = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: str = "decab"

    file_location: str = "python/Advent of Code/2016/Day 21/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, "abcde")

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
