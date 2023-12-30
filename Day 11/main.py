from __future__ import annotations
from itertools import combinations
from collections import defaultdict
OUTPUT_TYPE = int


class State:
    def __init__(self, locations: list[list[str]], floor: int, time: int) -> None:
        self.locations = locations
        self.floor = floor
        self.time = time

    def __str__(self) -> str:
        ret: str = ""
        ret += f"Time: {self.time}\n"
        for i, v in enumerate(self.locations[::-1]):
            floor: int = 3 - i
            if self.floor == floor:
                ret += f"[{floor}] "
            else:
                ret += f" {floor}  "

            for j in v:
                ret += j + " " * (4 - len(j))
            ret += "\n"
        return ret

    def __hash__(self) -> int:
        ret: int = 0
        for i, v in enumerate(self.locations):
            for a in v:
                ret += hash(a * (self.floor + 1)) << i
        return ret & 0xffffffff

    def is_valid(self) -> bool:
        for floor in self.locations:
            generators: set[str] = set()
            microchips: set[str] = set()
            for thing in floor:
                if thing[-1] == "G":
                    generators.add(thing[:-1])
                else:
                    microchips.add(thing[:-1])

            if len(generators) == 1 and len(microchips) == 2:
                pass

            chips_at_risk: set[str] = microchips.difference(generators)
            if len(chips_at_risk) == 0:
                continue

            if len(generators) == 0:
                continue

            return False

        return True

    def copy(self) -> State:
        return State(
            [floor.copy() for floor in self.locations],
            self.floor,
            self.time
        )

    def neighbours(self) -> list[State]:
        ret: list[State] = []
        for move in self.locations[self.floor]:
            for direction in [-1, 1]:
                new_state: State = self.copy()
                new_floor: int = self.floor + direction
                if new_floor < 0 or new_floor > 3:
                    continue

                new_state.locations[self.floor].remove(move)
                new_state.locations[new_floor].append(move)
                new_state.floor = new_floor
                new_state.time += 1
                ret.append(new_state)

        for move_1, move_2 in combinations(self.locations[self.floor], 2):
            for direction in [-1, 1]:
                new_state = self.copy()
                new_floor = self.floor + direction
                if new_floor < 0 or new_floor > 3:
                    continue

                new_state.locations[self.floor].remove(move_1)
                new_state.locations[self.floor].remove(move_2)
                new_state.locations[new_floor].append(move_1)
                new_state.locations[new_floor].append(move_2)
                new_state.floor = new_floor
                new_state.time += 1
                ret.append(new_state)

        return [state for state in ret if state.is_valid()]

    def complete(self) -> bool:
        return max(map(len, self.locations[:-1])) == 0


def parse_inp(inp: list[str], part: int = 1) -> State:
    floors: list[list[str]] = []
    for line in inp:
        obj: list[str] = []

        line = line.replace("nothing relevant", "")
        line = line.replace(".", "")
        line = line.replace("\n", "")
        line = line.replace(", and ", ", ")
        line = line.replace(" and ", ", ")
        line = line.split("contains ")[1]

        objects: list[str] = line.split(", ")
        for thing in objects:
            if not thing:
                continue

            desc: list[str] = thing.split(" ")
            obj.append((desc[1][:2] + desc[2][0]).upper())

        floors.append(obj)

    if part == 2:
        floors[0].extend(["ELG", "ELM", "DIG", "DIM"])

    return State(floors, 0, 0)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    states: list[State] = [parse_inp(inp)]
    best: defaultdict[int, int] = defaultdict(lambda: 100000000000000)
    source: dict[State, State] = {}
    best[hash(states[0])] = 0

    while states:
        active: State = states.pop(0)
        if active.complete():
            pos: State = active
            while pos.time != 0:
                pos = source[pos]
            return active.time

        for neighbour in active.neighbours():
            if best[hash(neighbour)] <= neighbour.time:
                continue

            best[hash(neighbour)] = neighbour.time
            source[neighbour] = active
            states.append(neighbour)
    return -1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    states: list[State] = [parse_inp(inp, 2)]
    best: defaultdict[int, int] = defaultdict(lambda: 100000000000000)
    source: dict[State, State] = {}
    best[hash(states[0])] = 0

    while states:
        active: State = states.pop(0)
        # print(active)
        if active.complete():
            pos: State = active
            # print(pos)
            while pos.time != 0:
                pos = source[pos]
                # print(pos)
            return active.time

        for neighbour in active.neighbours():
            if best[hash(neighbour)] <= neighbour.time:
                continue

            best[hash(neighbour)] = neighbour.time
            source[neighbour] = active
            states.append(neighbour)
#            print(neighbour)
    return -1


def main() -> None:
    test_input: str = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 11
    test_output_part_2_expected: OUTPUT_TYPE = -1

    file_location: str = "python/Advent of Code/2016/Day 11/input.txt"
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
