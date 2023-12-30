from collections import defaultdict
OUTPUT_TYPE = int


class CellularAutomata:
    def __init__(self, rule: list[bool], bounds: tuple[int, int]) -> None:
        self.rule: list[bool] = rule
        self.points: list[int] = []
        self.bounds: tuple[int, int] = bounds

    def safe(self) -> int:
        return self.bounds[1] - self.bounds[0] + 1 - len(self.points)

    def add_point(self, points: int | list[int]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.append(point)
        else:
            self.points.append(points)

    def in_bound(self, x: int) -> bool:
        return self.bounds[0] <= x and x <= self.bounds[1]

    def determine_future_point(self, x: int) -> bool:
        lookup: int = 0
        for x_diff in range(-1, 2):
            lookup = lookup << 1
            if x + x_diff in self.points:
                lookup = lookup + 1

        return self.rule[lookup]

    def tick(self) -> None:
        new_points: list[int] = []
        for x in range(self.bounds[0], self.bounds[1] + 1):
            if self.determine_future_point(x):
                new_points.append(x)

        self.points = new_points

    def __str__(self) -> str:
        ret: str = ""
        for x in range(self.bounds[0], self.bounds[1] + 1):
            if x in self.points:
                ret += "^"
            else:
                ret += "."

        return ret

    def __hash__(self) -> int:
        return int(str(self).replace(".", "0").replace("^", "1"), 2)


def main_part_1(inp: list[str], ticks: int = 40) -> OUTPUT_TYPE:
    points: list[int] = []
    for i, char in enumerate(inp[0]):
        if char == "^":
            points.append(i)

    cell: CellularAutomata = CellularAutomata(
        [False, True, False, True, True, False, True, False],
        (0, len(inp[0]) - 1)
    )

    cell.add_point(points)

    ret: int = 0
    for _ in range(ticks):
        ret += cell.safe()
        cell.tick()
        # print(cell)

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1(inp, 400000)


def main() -> None:
    test_input: str = """.^^.^.^^^^"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 38
    test_output_part_2_expected: OUTPUT_TYPE = 1935478

    file_location: str = "python/Advent of Code/2016/Day 18/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 10)
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
