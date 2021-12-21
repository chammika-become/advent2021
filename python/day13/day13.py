import re


def fold(points, fold_y=None, fold_x=None):
    if fold_y:
        # reflecting on Y
        stationay = set((x, y) for x, y in points if y < fold_y)
        reflected = set((x, y - 2 * (y - fold_y)) for x, y in points if y > fold_y)
        points = stationay | reflected
        print(f"After fold Y : {len(points)} points")
    elif fold_x:
        # reflecting on X
        stationay = set((x, y) for x, y in points if x < fold_x)
        reflected = set((x - 2 * (x - fold_x), y) for x, y in points if x > fold_x)
        points = stationay | reflected
        print(f"After fold X : {len(points)} points")
    return points


def print_paper(coords):
    max_x = max(x for x, _ in coords) + 1
    max_y = max(y for _, y in coords) + 1

    for i in range(max_y):
        for j in range(max_x):
            print(f"{'#' if (j, i) in coords else '.'}", end="")
        print("")
    print("")


def main():

    data = [line.strip() for line in open("./day13/input")]
    coords = [l for l in data if l != "" and not l.startswith("fold")]
    coords = set(tuple(map(int, l.split(","))) for l in coords)

    folds = [
        (re.search(r"(\w)=(\d+)", l).groups())
        for l in data
        if l.startswith("fold along ")
    ]
    folds = [(xy, int(c)) for xy, c in folds]
    print(folds)

    for xy, c in folds:
        if xy == "x":
            coords = fold(coords, fold_x=c)
        else:
            coords = fold(coords, fold_y=c)

    print_paper(coords)


if __name__ == "__main__":
    main()
