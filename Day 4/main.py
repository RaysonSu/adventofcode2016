OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for row in inp:
        row = row.strip()
        to_filter: str = row[-6:-1]
        room_id: int = int(row[-10:-7])
        data: str = row[:-11]

        counts: list[tuple[int, str]] = [
            (-data.count(char), char)
            for char in set(data)
            if char.isalpha()
        ]
        counts.sort()
        calced: str = "".join([char for _, char in counts])[:len(to_filter)]

        if calced == to_filter:
            ret += room_id
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    for row in inp:
        row = row.strip()
        room_id: int = int(row[-10:-7])
        data: str = row[:-11]

        for i in range(26):
            data = data.replace(chr(0x61 + i), chr(0x41 + (i + room_id) % 26))

        data = data.lower().replace("-", " ")

        if data == "northpole object storage":
            return room_id

    return -1


def main() -> None:
    test_input: str = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
qzmt-zixmtkozy-ivhz-343[abcde]"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1514
    test_output_part_2_expected: OUTPUT_TYPE = -1

    file_location: str = "python/Advent of Code/2016/Day 4/input.txt"
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
