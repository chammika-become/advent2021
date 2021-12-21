import collections
from typing import Dict


def apply_rules(template: str, rules: Dict[str, str]) -> str:
    insertions = {}
    for i in range(len(template) - 1):
        seg = template[i : i + 2]
        if seg in rules:
            insertions[i] = rules[seg]

    new_template = ""
    for i, p in enumerate(template):
        new_template += p + insertions.get(i, "")
    return new_template


def main():
    with open("./day14/input") as inp:
        template = next(inp).strip()
        _ = next(inp)
        rules = {}
        for l in inp:
            seq, insertion = l.strip().split(" -> ")
            rules[seq] = insertion
    print(f"Strating template : {template}")

    steps = 10
    for i in range(steps):
        template = apply_rules(template, rules)
        # print(f"Step {i+1} len({len(template)}): {template}")

    stats = dict(collections.Counter(template))
    max_freq = max(freq for freq in stats.values())
    min_freq = min(freq for freq in stats.values())
    print(f"#most common element - #least common element : {max_freq-min_freq}")


if __name__ == "__main__":
    main()
