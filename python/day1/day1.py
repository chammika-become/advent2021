def main():
    depths = [int(l) for l in open("./day1/input")]
    prev = depths[0]
    cnt = 0
    for depth in depths[1:]:
        if depth > prev:
            cnt += 1
        prev = depth
    print(f"Depth increases:  {cnt}")


if __name__ == "__main__":
    main()
