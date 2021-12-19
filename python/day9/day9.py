def main():
    heightmap = []
    with open("./day9/input") as inp:
        for l in inp:
            heightmap.append([int(v) for v in l.strip()])
    print(heightmap)
    N = len(heightmap)
    M = len(heightmap[0])
    risk_level = 0

    def basin_explore(r, c, basin):
        if not 0 <= r < N or not 0 <= c < M or (r, c) in basin or heightmap[r][c] == 9:
            return
        else:
            basin.add((r, c))
            basin_explore(r + 1, c, basin)
            basin_explore(r, c + 1, basin)
            basin_explore(r - 1, c, basin)
            basin_explore(r, c - 1, basin)

    basin_sizes = []
    for i in range(N):
        for j in range(M):
            val = heightmap[i][j]
            if (
                (i > 0 and val >= heightmap[i - 1][j])
                or (i < N - 1 and val >= heightmap[i + 1][j])
                or (j > 0 and val >= heightmap[i][j - 1])
                or (j < M - 1 and val >= heightmap[i][j + 1])
            ):
                pass
            else:
                risk_level += 1 + val
                basin = set()
                basin_explore(i, j, basin)
                basin_sizes.append(len(basin))
    print(f"Risk level : {risk_level}")
    basin_sizes.sort(reverse=True)
    l3prod = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(f"Largest 3 basin sizes multiplied : {l3prod}")
    print(f"Basin sizes : {basin_sizes}")


if __name__ == "__main__":
    main()
