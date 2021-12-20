from collections import defaultdict
from typing import Dict, List


def find_paths(network: Dict[str, List[str]], start: str, dest: str):
    def is_small_cave(node: str) -> bool:
        return node != node.upper()

    def cannot_visit_node(node: str, path: List[str]) -> bool:
        return is_small_cave(node) and node in path

    path_count = 0
    repeating_node = None  # Only for part 2

    def find_dfs(node, path) -> None:
        nonlocal network
        nonlocal dest
        nonlocal path_count
        nonlocal repeating_node

        for adj_node in network[node]:
            if cannot_visit_node(adj_node, path):
                # part 1 : just continue at this point
                # continue

                # part 2 : check for repeating_node
                if repeating_node:
                    continue
                else:
                    repeating_node = adj_node
            path.append(adj_node)
            if adj_node == dest:
                print(",".join(path))
                path_count += 1
            else:
                find_dfs(adj_node, path)
            n = path.pop()
            if n == repeating_node:  # Only for part 2
                repeating_node = None

    find_dfs(start, [start])
    print(f"Total number of paths : {path_count}")


def main():
    lines = [line.strip().split("-") for line in open("./day12/input")]
    network = defaultdict(lambda: [])
    for cave1, cave2 in lines:
        # Remove start from adjusceny list of any node
        if cave2 != "start":
            network[cave1].append(cave2)
        if cave1 != "start":
            network[cave2].append(cave1)
    start = "start"
    dest = "end"
    print(network)
    find_paths(network, start, dest)


if __name__ == "__main__":
    main()
