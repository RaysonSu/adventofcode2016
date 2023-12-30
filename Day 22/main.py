from __future__ import annotations
from itertools import permutations
from typing import Any
OUTPUT_TYPE = int


class State:
    def __init__(self, grid: list[str], goal_tile: tuple[int, int], empty_tile: tuple[int, int], time: int) -> None:
        self.grid: list[str] = grid
        self.goal_tile: tuple[int, int] = goal_tile
        self.empty_tile: tuple[int, int] = empty_tile
        self.time: int = time

    def __str__(self) -> str:
        return f"{self.goal_tile}//{self.empty_tile}"

    def finished(self) -> bool:
        return self.goal_tile == (0, 0)

    def neighbours(self) -> list[State]:
        ret: list[State] = []

        for x_diff, y_diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_location = (
                self.empty_tile[0] + x_diff,
                self.empty_tile[1] + y_diff
            )

            if new_location[0] < 0 or new_location[0] >= len(self.grid[0]):
                continue

            if new_location[1] < 0 or new_location[1] >= len(self.grid):
                continue

            tile: str = self.grid[new_location[1]][new_location[0]]

            if tile == "#":
                continue

            new_goal: tuple[int, int] = self.goal_tile
            if new_goal == new_location:
                new_goal = self.empty_tile

            ret.append(State(
                self.grid,
                new_goal,
                new_location,
                self.time + 1
            ))

        return ret


def parse_inp(inp: list[str]) -> list[list[tuple[int, int]]]:
    inp = inp[2:]
    lengths: str = inp[-1][:23]
    x_length: int = int(lengths.split("-")[1][1:]) + 1
    y_length: int = int(lengths.split("-")[2][1:]) + 1
    ret: list[list[tuple[int, int]]] = []
    for x in range(x_length):
        col: list[tuple[int, int]] = []
        for y in range(y_length):
            data: list[str] = [
                char for char in inp[y_length * x + y].split(" ") if char]
            col.append((int(data[2][:-1]), int(data[3][:-1])))
        ret.append(col)
    return transpose_2d_list(ret)


def transpose_2d_list(grid: list[list[Any]]) -> list[list[Any]]:
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: list[list[tuple[int, int]]] = parse_inp(inp)
    flatten: list[tuple[int, int]] = [node for row in data for node in row]

    ret: int = 0
    for x, y in permutations(flatten, 2):
        if x[0] <= y[1] and x[0] != 0:
            ret += 1

    return ret


def main_part_2(inp: list[str], obj: int = 100) -> OUTPUT_TYPE:
    data: list[list[tuple[int, int]]] = parse_inp(inp)
    grid: list[str] = [
        "".join(
            ["." if used < obj else "#" for used, _ in row]
        ) for row in data
    ]

    empty: tuple[int, int]
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char[0] == 0:
                empty = (j, i)

    states: list[State] = [State(grid, (len(grid[0]) - 1, 0), empty, 0)]
    seen: set[str] = {str(states[0])}
    while states:
        active: State = states.pop(0)

        if active.finished():
            return active.time

        for neighbour in active.neighbours():
            if str(neighbour) in seen:
                continue

            states.append(neighbour)
            seen.add(str(neighbour))

    return -1


def main() -> None:
    test_input: str = """root@ebhq-gridcenter# df -h
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_2_expected: OUTPUT_TYPE = 7

    file_location: str = "python/Advent of Code/2016/Day 22/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed, 28)

    print(f"Part 1: {main_part_1(input_file)}")

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
