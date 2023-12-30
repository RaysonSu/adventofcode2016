from __future__ import annotations
from collections import deque, defaultdict

OUTPUT_TYPE = int


class State:
    def __init__(self, grid: list[str], location: tuple[int, int] | None = None, time: int = 0, prev: int = -1, keys: str = "") -> None:
        self.grid: list[str] = grid
        if location:
            self.location: tuple[int, int] = location
        else:
            for row_index, row in enumerate(grid):
                if "0" in row:
                    self.location = (row.index("0"), row_index)
                    break
        self.time: int = time
        self.keys: str = keys
        self.prev: int = prev

    def neighbours(self) -> list[State]:
        ret: list[State] = []
        for direction in range(4):
            if self.prev == (direction + 2) % 4:
                continue

            new_location: tuple[int, int] = (
                self.location[0] + [1, 0, -1, 0][direction],
                self.location[1] + [0, -1, 0, 1][direction]
            )

            tile: str = self.grid[new_location[1]][new_location[0]]
            if tile == "#":
                continue

            if tile.isnumeric() and tile != "0" and tile not in self.keys:
                ret.append(State(
                    self.grid,
                    new_location,
                    self.time + 1,
                    -1,
                    self.keys + tile
                ))
                continue

            ret.append(State(
                self.grid,
                new_location,
                self.time + 1,
                direction,
                self.keys
            ))

        if ret == []:
            ret.append(State(
                self.grid,
                self.location,
                self.time + 1,
                self.prev,
                self.keys
            ))

        return ret

    def copy(self) -> State:
        return State(
            self.grid,
            self.location,
            self.time,
            self.prev,
            self.keys
        )

    def __hash__(self) -> int:
        return hash(str(self.location)) + sum([(23 + ord(x)) ** 6 for x in self.keys])


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    states: deque[State] = deque()
    best: defaultdict[int, int] = defaultdict(lambda: 10 ** 6)
    states.append(State(list(map(str.strip, inp))))
    count: int = -1
    for i in set("".join(inp)):
        if i.isnumeric():
            count += 1

    while states:
        active: State = states.popleft()
        neighbours: list[State] = active.neighbours()
        for neighbour in neighbours:
            if len(neighbour.keys) == count:
                # print()
                return neighbour.time

            hashed: int = hash(neighbour)
            if best[hashed] <= neighbour.time:
                continue

            best[hashed] = neighbour.time

            states.append(neighbour)

        del active
    return -1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    states: deque[State] = deque()
    best: defaultdict[int, int] = defaultdict(lambda: 10 ** 6)
    states.append(State(list(map(str.strip, inp))))
    goal: tuple[int, int] = states[0].location
    count: int = -1
    for i in set("".join(inp)):
        if i.isnumeric():
            count += 1

    while states:
        active: State = states.popleft()
        neighbours: list[State] = active.neighbours()
        for neighbour in neighbours:
            if len(neighbour.keys) == count and neighbour.location == goal:
                return neighbour.time

            hashed: int = hash(neighbour)
            if best[hashed] <= neighbour.time:
                continue

            best[hashed] = neighbour.time

            states.append(neighbour)

        del active
    return -1


def main() -> None:
    test_input: str = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 14
    test_output_part_2_expected: OUTPUT_TYPE = 20

    file_location: str = "python/Advent of Code/2016/Day 24/input.txt"
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
