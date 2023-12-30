def make_grid(x_len: int, y_len: int) -> list[list[int]]:
    return [
        [0 for _ in range(x_len)]
        for _ in range(y_len)
    ]


def str_grid(grid: list[list[int]]) -> str:
    ret: str = "\n"
    for row in grid:
        for char in row:
            if char:
                ret += "#"
            else:
                ret += " "
        ret += "\n"

    return ret


def rect(grid: list[list[int]], a: int, b: int) -> None:
    for y in range(b):
        for x in range(a):
            grid[y][x] = 1


def rotate_x(grid: list[list[int]], col: int, amt: int) -> None:
    data: list[int] = [grid[i][col] for i in range(len(grid))]
    data = data[-amt:] + data[:-amt]

    for i in range(len(grid)):
        grid[i][col] = data[i]


def rotate_y(grid: list[list[int]], row: int, amt: int) -> None:
    data: list[int] = [grid[row][i] for i in range(len(grid[row]))]
    data = data[-amt:] + data[:-amt]

    for i in range(len(grid[row])):
        grid[row][i] = data[i]


def main_part_1(inp: list[str], x_len: int = 50, y_len: int = 6) -> int:
    grid: list[list[int]] = make_grid(x_len, y_len)
    for row in inp:
        data: list[int] = [
            int(x)
            for x in "".join([
                char.replace("x", " ")
                for char in row
                if char.isnumeric() or char in "- x"
            ]).split(" ")
            if x != ""
        ]

        if "rect" in row:
            rect(grid, data[0], data[1])
        elif "col" in row:
            rotate_x(grid, data[0], data[1])
        elif "row" in row:
            rotate_y(grid, data[0], data[1])

    return sum(map(sum, grid))


def main_part_2(inp: list[str]) -> str:
    grid: list[list[int]] = make_grid(50, 6)
    for row in inp:
        data: list[int] = [
            int(x)
            for x in "".join([
                char.replace("x", " ")
                for char in row
                if char.isnumeric() or char in "- x"
            ]).split(" ")
            if x != ""
        ]

        if "rect" in row:
            rect(grid, data[0], data[1])
        elif "col" in row:
            rotate_x(grid, data[0], data[1])
        elif "row" in row:
            rotate_y(grid, data[0], data[1])

    return str_grid(grid)


def main() -> None:
    test_input: str = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: int = 6

    file_location: str = "python/Advent of Code/2016/Day 8/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: int = main_part_1(test_input_parsed, 7, 3)

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
