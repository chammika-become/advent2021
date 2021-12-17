def main():
    codes = [l.strip() for l in open("./day3/input")]
    N = len(codes)
    L = len(codes[0])
    ones = [0] * L
    for code in codes:
        for i, c in enumerate(code):
            if c == "1":
                ones[i] += 1
    gamma_rate, epsilon_rate = 0, 0
    for n in ones:
        gamma_rate <<= 1
        epsilon_rate <<= 1
        if n > N // 2:
            gamma_rate += 1
        else:
            epsilon_rate += 1
    print(f"Engery consumption : {gamma_rate*epsilon_rate}")


if __name__ == "__main__":
    main()
