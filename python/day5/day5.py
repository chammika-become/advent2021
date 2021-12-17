import re


def part_two(coords):
    max_x = max((max(x1, x2) for x1, _, x2, _ in coords)) + 1
    max_y = max((max(y1, y2) for _, y1, _, y2 in coords)) + 1

    board = [[0] * max_x for _ in range(max_y)]

    for x1, y1, x2, y2 in coords:
        xstep = 0 if x1 == x2 else 1 if x1 < x2 else -1
        ystep = 0 if y1 == y2 else 1 if y1 < y2 else -1
        x, y = x1, y1
        while x != x2 + xstep or y != y2 + ystep:
            board[y][x] += 1
            x += xstep
            y += ystep
    points = sum(1 for i in range(max_x) for j in range(max_y) if board[i][j] >= 2)
    print(f"Point with more than 2 lines overlapping: {points}")


def part_one(coords):
    xy_coords = [(x1, y1, x2, y2) for x1, y1, x2, y2 in coords if x1 == x2 or y1 == y2]

    max_x = max((max(x1, x2) for x1, _, x2, _ in xy_coords)) + 1
    max_y = max((max(y1, y2) for _, y1, _, y2 in xy_coords)) + 1

    board = [[0] * max_x for _ in range(max_y)]

    for x1, y1, x2, y2 in xy_coords:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                board[x1][y] += 1
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                board[x][y1] += 1
    points = sum(1 for i in range(max_x) for j in range(max_y) if board[i][j] >= 2)
    print(f"Point with more than 2 lines overlapping: {points}")


def main():
    coords = []
    with open("./day5/input") as inp:
        for l in inp:
            x1, y1, x2, y2 = map(
                int, re.search(r"(\d+),(\d+) -> (\d+),(\d+)", l).groups()
            )
            coords.append((x1, y1, x2, y2))

    part_one(coords)
    part_two(coords)


if __name__ == "__main__":
    main()
