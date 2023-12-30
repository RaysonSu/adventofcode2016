from hashlib import md5 as md
import re
OUTPUT_TYPE = int


def md5(string: str, reps: int = 1) -> str:
    for _ in range(reps):
        string = md(string.encode()).hexdigest()
    return string


def main_part_1(inp: str) -> OUTPUT_TYPE:
    keys_found: list[int] = []
    key_buf: list[list[int]] = [[] for _ in range(16)]
    key_check: int = 0

    has_three: re.Pattern = re.compile("([\d|a-f])\\1{2,}")
    has_five: re.Pattern = re.compile("([\d|a-f])\\1{4,}")

    end: int = -1
    while key_check < end or end == -1:
        hashed: str = md5(inp + str(key_check))

        for i in has_five.findall(hashed):
            validated: list[int] = key_buf[int(i, 16)]
            # print(f"\033[2K\033[1GQuintuple found: {key_check} {i}")
            # for val in validated:
            #     print(f"\033[2K\033[1GTriple validated: {val}")
            keys_found.extend(validated)
            key_buf[int(i, 16)] = []

        for i in has_three.findall(hashed)[:1]:
            # print(f"\033[2K\033[1GTriple found: {key_check} {i}")
            key_buf[int(i, 16)].append(key_check)

        for buf in key_buf:
            if not buf:
                continue

            if buf[0] + 1000 <= key_check:
                buf.pop(0)

        if len(keys_found) >= 64 and end == -1:
            end = key_check + 1000

        key_check += 1
#        print("\r" + str(key_check), str(keys_found), end="")
    keys_found.sort()
#    print(keys_found)
    return keys_found[63]


def main_part_2(inp: str) -> OUTPUT_TYPE:
    keys_found: list[int] = []
    key_buf: list[list[int]] = [[] for _ in range(16)]
    key_check: int = 0

    has_three: re.Pattern = re.compile("([\d|a-f])\\1{2,}")
    has_five: re.Pattern = re.compile("([\d|a-f])\\1{4,}")

    end: int = -1
    while key_check < end or end == -1:
        hashed: str = md5(inp + str(key_check), 2017)

        for i in has_five.findall(hashed):
            validated: list[int] = key_buf[int(i, 16)]
            # print(f"\033[2K\033[1GQuintuple found: {key_check} {i}")
            # for val in validated:
            #     print(f"\033[2K\033[1GTriple validated: {val}")
            keys_found.extend(validated)
            key_buf[int(i, 16)] = []

        for i in has_three.findall(hashed)[:1]:
            # print(f"\033[2K\033[1GTriple found: {key_check} {i}")
            key_buf[int(i, 16)].append(key_check)

        for buf in key_buf:
            if not buf:
                continue

            if buf[0] + 1000 <= key_check:
                buf.pop(0)

        if len(keys_found) >= 64 and end == -1:
            end = key_check + 3000

        key_check += 1
#        print("\r" + str(key_check), str(keys_found), end="")
    keys_found.sort()
#    print(keys_found)
    return keys_found[63]


def main() -> None:
    test_input: str = "zpqevtbw"
    test_output_part_1_expected: OUTPUT_TYPE = 16106
    test_output_part_2_expected: OUTPUT_TYPE = 22423

    file_location: str = "python/Advent of Code/2016/Day 14/input.txt"
    input_file: str = open(file_location).read()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input)

    if test_output_part_1_expected == test_output_part_1:
        print(f"\rPart 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"\rPart 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()

# Triple validated: 21179
# Triple validated: 21441
# Triple validated: 21554
# Triple validated: 21590
# Triple validated: 21651
# Triple validated: 21701
# Triple validated: 21792
# Triple validated: 21901
# Triple validated: 21939
# Triple validated: 21943
# Triple validated: 21989
# Triple validated: 22034
# Triple validated: 22045
# Triple validated: 22065
# Triple validated: 22330
[804, 1097, 1230, 1288,
 1394, 4182, 4624, 4827,
 4915, 5027, 5035, 10092,
 10617, 10694, 10772, 10823,
 11210, 11230, 11277, 11312,
 11318, 11370, 11452, 11499,
 11513, 11716, 11728, 11878,
 12034, 12115, 12126, 15343,
 15417, 15768, 15770, 15848,
 15876, 16068, 16102, 16217,
 16518, 16874, 20293, 20440,
 20496, 20497, 20692, 21045,
 21050, 21106, 21124, 21134,
 21179, 21441, 21554, 21590,
 21651, 21701, 21792, 21901,
 21939, 21943, 21989, 22034,
 22045, 22065, 22330]
