import sys


def main():
    positions = [int(v) for v in open("./day7/input").read().strip().split(",")]
    max_pos, min_pos = max(positions), min(positions)
    min_dist = sys.maxsize

    for i, l in enumerate(range(min_pos, max_pos + 1)):
        # part1 distance
        # dist = sum(abs(p - l) for p in positions)
        # part2 distance: d(d+1)/2
        dist = sum((abs(p - l) * (abs(p - l) + 1)) // 2 for p in positions)
        print(f"{i} iteration : {dist} {min_dist} delta {dist-min_dist}")
        min_dist = min(dist, min_dist)
        if dist > min_dist:
            break

    print(f"Minimum fuel to align : {min_dist}")


if __name__ == "__main__":
    main()
