from typing import List

seg2digit = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def solve(patterns: List[str], output: List[str]) -> List[int]:
    patterns = [set(pat) for pat in patterns]

    # find a => patterns for 7 - patterns for 1
    pat_1 = [pat for pat in patterns if len(pat) == 2][0]
    pat_7 = [pat for pat in patterns if len(pat) == 3][0]
    a = pat_7 - pat_1
    # print(f"a => {a}")

    # find bd => patterns for 4 - patterns for 1
    pat_4 = [pat for pat in patterns if len(pat) == 4][0]
    bd = pat_4 - pat_1
    # print(f"bd => {bd}")

    # find adg => common patterns in 2, 3, 5 (each has 5 segments)
    pat_235 = [pat for pat in patterns if len(pat) == 5]
    adg = pat_235[0] & pat_235[1] & pat_235[2]
    # print(f"adg => {adg}")

    dg = adg - a
    d = dg & bd
    g = dg - d
    b = bd - d
    # print(f"d => {d}, g => {g}, b => {b}")

    # find abfg => common patterns for 0, 6, 9 (each has 6 segments)
    pat_069 = [pat for pat in patterns if len(pat) == 6]
    abfg = pat_069[0] & pat_069[1] & pat_069[2]
    # print(f"abfg => {abfg}")

    f = abfg - (a | b | g)
    # print(f"f => {f}")

    cf = pat_1
    c = cf - f
    # print(f"c => {c}")

    e = set("abcdefg") - (a | b | c | d | f | g)
    # print(f"e => {e}")

    mapping = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g}
    # convert set to segment and reverse the mapping to use
    mapping = {next(iter(v)): k for k, v in mapping.items()}

    nums = []
    for digit in output:
        segments = "".join(sorted([mapping[s] for s in digit]))
        nums.append(seg2digit[segments])

    return nums


def main():
    puzzles = []
    with open("./day8/input") as inp:
        for l in inp:
            patterns, output = l.strip().split("|")
            patterns = [set(pat) for pat in patterns.strip().split(" ")]
            output = output.strip().split(" ")
            puzzles.append((patterns, output))

    count_1478 = 0
    output_sum = 0
    for patterns, output in puzzles:
        res = solve(patterns, output)
        print(f"{res}")
        count_1478 += sum(1 for d in res if d in [1, 4, 7, 8])
        output_sum += 1000 * res[0] + 100 * res[1] + 10 * res[2] + res[3]
    print(f"Count of 1, 4, 7, 8 : {count_1478}")
    print(f"Sum of output numbers : {output_sum}")


if __name__ == "__main__":
    main()
