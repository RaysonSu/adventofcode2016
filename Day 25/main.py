OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    index: int = 0
    while True:
        regs: dict[str, int] = {"a": index, "b": 0, "c": 0, "d": 0}
        instruction: int = 0
        outputs: int = 1
        counts: int = 0

        while True:
            if counts == 100:
                return index

            if instruction >= len(inp):
                break

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
            elif chars[0] == "out":
                if chars[1].isnumeric():
                    value = int(chars[1])
                else:
                    value = regs[chars[1]]

                if outputs == 1 - value:
                    outputs = value
                    counts += 1
                else:
                    break

            if not jumped:
                instruction += 1

        index += 1


def main() -> None:
    file_location: str = "python/Advent of Code/2016/Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file.copy())}")


if __name__ == "__main__":
    main()


# a = 0
# d = a
# c = 7
# while c:
#     b = 365
#     while b:
#         d += 1
#         b -= 1
#     c -= 1

# while True:
#     a = d
#     while a:
#         b = a
#         a = 0

#         while True:
#             c = 2
#             while c:
#                 if not b:
#                     break

#                 b -= 1
#                 c -= 1
#             else:
#                 a += 1
#                 continue

#             break

#         b = 2
#         while c:
#             b -= 1
#             c -= 1
#         input(b)
