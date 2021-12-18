import collections
from typing import DefaultDict


def main():
    fish = [int(v) for v in open("./day6/input").read().strip().split(",")]
    freq = {k: sum(1 for v in fish if v == k) for k in range(9)}

    steps = 256
    print(f"Starting Fish : {freq}")
    for i in range(steps):
        new_freq = {k - 1: f for k, f in freq.items() if 0 < k <= 6}
        new_freq[6] = freq[0] + freq[7]
        new_freq[7] = freq[8]
        new_freq[8] = freq[0]
        freq = new_freq
        print(f"({i+1}) New population: {freq} : {sum(freq.values())}")


if __name__ == "__main__":
    main()
