from collections import defaultdict
OUTPUT_TYPE = int


def main_part_1(inp: list[str], chip_1: int, chip_2: int) -> OUTPUT_TYPE:
    inp.sort(reverse=True)
    for index in range(len(inp)):
        output: int = 0
        while "output" in inp[index]:
            inp[index] = inp[index].replace(
                f"output {output}", f"bot {-1-output}")
            output += 1

    bots: defaultdict[int, set[int]] = defaultdict(lambda: set())
    for i in inp:
        if i.startswith("value"):
            bots[int(i.split(" ")[-1])].add(int(i.split(" ")[1]))

    while True:
        try:
            for bot, values in bots.items():
                if len(values) != 2:
                    continue

                for i in inp:
                    if i.startswith("value"):
                        continue

                    if int(i.split(" ")[1]) != bot:
                        continue

                    bots[int(i.split(" ")[6])].add(min(values))
                    bots[int(i.split(" ")[-1])].add(max(values))

                    bots[bot] = set()

                    if values == {chip_1, chip_2}:
                        return bot
        except RuntimeError as _:
            pass


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp.sort(reverse=True)
    for index in range(len(inp)):
        output: int = 0
        while "output" in inp[index]:
            inp[index] = inp[index].replace(
                f"output {output}", f"bot {-1-output}")
            output += 1

    bots: defaultdict[int, set[int]] = defaultdict(lambda: set())
    for i in inp:
        if i.startswith("value"):
            bots[int(i.split(" ")[-1])].add(int(i.split(" ")[1]))

    while True:
        try:
            for bot, values in bots.items():
                if len(values) != 2:
                    continue

                for i in inp:
                    if i.startswith("value"):
                        continue

                    if int(i.split(" ")[1]) != bot:
                        continue

                    bots[int(i.split(" ")[6])].add(min(values))
                    bots[int(i.split(" ")[-1])].add(max(values))

                    bots[bot] = set()
        except RuntimeError as _:
            pass

        if max(map(len, bots.values())) == 1:
            return bots[-1].pop() * bots[-2].pop() * bots[-3].pop()


def main() -> None:
    test_input: str = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 2
    test_output_part_2_expected: OUTPUT_TYPE = 30

    file_location: str = "python/Advent of Code/2016/Day 10/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 5, 2)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file, 61, 17)}")
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
