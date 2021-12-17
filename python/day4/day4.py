from typing import List, Optional, Dict, Tuple, Any


def main():
    with open("./day4/input") as inp:
        draws = next(inp)
        draws = map(int, draws.strip().split(","))
        _ = next(inp)
        lines = []
        for l in inp:
            lines.append(l.strip())

        puzzles = {}
        for k, p in enumerate(range(0, len(lines), 6)):
            puzzle = {
                int(v): (i, j)
                for i in range(5)
                for j, v in enumerate(lines[p + i].replace("  ", " ").split(" "))
            }
            puzzles[k] = puzzle

    solutions = [[0] * 10 for _ in range(len(puzzles))]

    for draw in draws:
        winning_puzzles = []
        for i in puzzles.keys():
            puzzle = puzzles[i]
            if draw in puzzle:
                row, col = puzzle[draw]
                sol = solutions[i]
                sol[row] |= 1 << col
                sol[5 + col] |= 1 << row
                puzzle.pop(draw)
                if any(s == 31 for s in sol):
                    print(f"{i}-puzzle : Solution : {sum(puzzle.keys())*draw}")
                    winning_puzzles.append(i)
        if winning_puzzles:
            for i in winning_puzzles:
                puzzles.pop(i)


if __name__ == "__main__":
    main()
