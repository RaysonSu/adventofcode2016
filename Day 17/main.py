from __future__ import annotations
from hashlib import md5 as md


class State:
    def __init__(self, key: str, path: str) -> None:
        self.key: str = key
        self.path: str = path

    def location(self) -> tuple[int, int]:
        return (
            self.path.count("R") - self.path.count("L"),
            self.path.count("D") - self.path.count("U")
        )

    def is_finished(self) -> bool:
        return self.location() == (3, 3)

    def is_valid(self) -> bool:
        x: int
        y: int
        x, y = self.location()
        return x >= 0 and y >= 0 and x < 4 and y < 4

    def neighbours(self) -> list[State]:
        hashed: str = md5(self.key + self.path)
        ret: list[State] = []
        for index, path in enumerate("UDLR"):
            if hashed[index] not in "bcdef":
                continue

            new_state: State = State(
                self.key,
                self.path + path
            )

            if not new_state.is_valid():
                continue

            ret.append(new_state)

        return ret


def md5(string: str, reps: int = 1) -> str:
    for _ in range(reps):
        string = md(string.encode()).hexdigest()
    return string


def main_part_1(inp: list[str]) -> str:
    states: list[State] = [State(inp[0].strip(), "")]
    while states:
        active: State = states.pop(0)

        if active.is_finished():
            return active.path

        states.extend(active.neighbours())

    return ""


def main_part_2(inp: list[str]) -> int:
    states: list[State] = [State(inp[0].strip(), "")]
    best: int = 0

    while states:
        active: State = states.pop(0)

        if active.is_finished():
            best = max(best, len(active.path))
            continue

        states.extend(active.neighbours())

    return best


def main() -> None:
    test_input: str = """ihgpwlah"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: str = "DDRRRD"
    test_output_part_2_expected: int = 370

    file_location: str = "python/Advent of Code/2016/Day 17/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: str = main_part_1(test_input_parsed)
    test_output_part_2: int = main_part_2(test_input_parsed)

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
        print()


if __name__ == "__main__":
    main()
