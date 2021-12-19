import itertools


def simulate_step(board) -> int:
    # 1. increase energy by 1
    N, M = len(board), len(board[0])
    for i in range(N):
        for j in range(M):
            board[i][j] += 1

    # 2. Flash if energy > 9
    flashed = set()

    def disperse_energy(r, c):
        if 0 <= r < N and 0 <= c < M:
            board[r][c] += 1

    def flash_dfs(r, c):
        if not 0 <= r < N or not 0 <= c < M or board[r][c] <= 9 or (r, c) in flashed:
            return
        disperse_energy(r, c + 1)  # right
        disperse_energy(r, c - 1)  # left
        disperse_energy(r - 1, c)  # up
        disperse_energy(r + 1, c)  # down
        disperse_energy(r - 1, c + 1)  # right-up
        disperse_energy(r + 1, c + 1)  # right-down
        disperse_energy(r - 1, c - 1)  # left-up
        disperse_energy(r + 1, c - 1)  # left-down
        flashed.add((r, c))
        # propagate flash
        flash_dfs(r, c + 1)  # right
        flash_dfs(r, c - 1)  # left
        flash_dfs(r - 1, c)  # up
        flash_dfs(r + 1, c)  # down
        flash_dfs(r - 1, c + 1)  # right-up
        flash_dfs(r + 1, c + 1)  # right-down
        flash_dfs(r - 1, c - 1)  # left-up
        flash_dfs(r + 1, c - 1)  # left-down

    for i in range(N):
        for j in range(M):
            flash_dfs(i, j)

    # 3. Reset flashed ocutupus engery to 0
    for r, c in flashed:
        board[r][c] = 0

    return len(flashed)


def print_board(board):
    for row in board:
        print(row)


def part_one(board):
    steps = 100
    total_flashes = 0
    for i in range(steps):
        flashes = simulate_step(board)
        total_flashes += flashes
        print(f"Flashed in simulatiion step {i+1} : {flashes} total {total_flashes}")
        print_board(board)


def part_two(board):
    def all_flashed(board):
        for row in board:
            if not all(v == 0 for v in row):
                return False
        return True

    for i in itertools.count(start=1):
        _ = simulate_step(board)
        if all_flashed(board):
            print(f"All flashed in step : {i}")
            break


def main():
    lines = [line.strip() for line in open("./day11/input")]
    board = []
    for line in lines:
        board.append([int(v) for v in line])

    # part_one(board.copy())
    part_two(board)


if __name__ == "__main__":
    main()
