def main():
    depths = [int(l) for l in open("./day1/input")]
    window_depths = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
    prev = window_depths[0]
    cnt = 0
    for depth in window_depths[1:]:
        if depth > prev:
            cnt += 1
        prev = depth
    print(f"Depth increases:  {cnt}")


if __name__ == "__main__":
    main()
