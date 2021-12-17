from typing import List, Optional


def common_value(codes: List[str], pos: int) -> Optional[str]:
    ones = sum(1 for c in codes if c[pos] == "1")
    if 2 * ones > len(codes):
        return "1"
    elif 2 * ones < len(codes):
        return "0"
    else:
        return None


def main():
    codes = [l.strip() for l in open("./day3/input")]

    N = len(codes)
    L = len(codes[0])

    o2_candidates = codes.copy()
    co2_candidates = codes.copy()
    for p in range(L):
        common = common_value(o2_candidates, p)
        if common == "1" or common == None:
            o2_candidates = [c for c in o2_candidates if c[p] == "1"]
        else:
            o2_candidates = [c for c in o2_candidates if c[p] == "0"]

        if len(o2_candidates) == 1:
            break

    for p in range(L):
        common = common_value(co2_candidates, p)
        if common == "0":
            co2_candidates = [c for c in co2_candidates if c[p] == "1"]
        else:
            co2_candidates = [c for c in co2_candidates if c[p] == "0"]
        if len(co2_candidates) == 1:
            break

    o2_num, co2_num = 0, 0
    for x, y in zip(o2_candidates[0], co2_candidates[0]):
        o2_num = (o2_num << 1) + int(x)
        co2_num = (co2_num << 1) + int(y)

    print(f"Engery consumption : {o2_num*co2_num}")


if __name__ == "__main__":
    main()
