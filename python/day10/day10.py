from typing import Union


def main():
    lines = [l.strip() for l in open("./day10/input")]

    open2close = {"(": ")", "[": "]", "{": "}", "<": ">"}
    illegal2points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    incomplete2points = {")": 1, "]": 2, "}": 3, ">": 4}

    def check_syntax(line) -> int:
        closing = []
        for c in line:
            if c in ["(", "[", "{", "<"]:
                closing.append(open2close[c])
            elif c != closing[-1]:
                return illegal2points[c]
            else:
                closing.pop()
        return 0  # correct or incomplete

    def check_incomplete(line) -> int:
        closing = []
        for c in line:
            if c in ["(", "[", "{", "<"]:
                closing.append(open2close[c])
            elif c != closing[-1]:
                return 0  # this is illigal sytax case
            else:
                closing.pop()
        score = 0
        while closing:
            score *= 5
            score += incomplete2points[closing.pop()]
        return score

    points = 0
    for line in lines:
        points += check_syntax(line)
    print(f"Total points for illigal closing : {points}")

    points = []
    for line in lines:
        res = check_incomplete(line)
        if res != 0:
            points.append(res)
    points.sort()
    print(f"Middle score of incomplete closings : {points[len(points)//2]}")


if __name__ == "__main__":
    main()
