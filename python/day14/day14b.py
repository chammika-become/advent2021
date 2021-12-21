from collections import defaultdict
from typing import Dict


def apply_rules(
    template_pairs: Dict[str, int], rules: Dict[str, str]
) -> Dict[str, int]:
    updates = []
    for pair in template_pairs:
        if pair in rules:
            updates.append(
                (
                    pair,  # delete this pair
                    template_pairs[pair],  # with original pair's freq
                    pair[0] + rules[pair],  # create new pair1
                    rules[pair] + pair[1],  # and pair2
                )
            )
    # delete all before inserting
    for pair, _, _, _ in updates:
        template_pairs.pop(pair)
    # insert new keys with same freq as old deleted-pair
    for _, freq, new_pair1, new_pair2 in updates:
        template_pairs[new_pair1] += freq
        template_pairs[new_pair2] += freq

    return template_pairs


def main():
    with open("./day14/input") as inp:
        template = next(inp).strip()
        _ = next(inp)
        rules = {}
        for l in inp:
            seq, insertion = l.strip().split(" -> ")
            rules[seq] = insertion

    template_pairs = defaultdict(lambda: 0)
    for i in range(len(template) - 1):
        template_pairs[template[i : i + 2]] += 1
    # print(f"Pairs in starting template : {template_pairs}")

    steps = 40
    for i in range(steps):
        template_pairs = apply_rules(template_pairs, rules)
        print(f"Step {i+1} len({len(template_pairs)}): {dict(template_pairs)}")

    char_stats = defaultdict(lambda: 0)
    for pair, freq in template_pairs.items():
        char_stats[pair[0]] += freq
        char_stats[pair[1]] += freq
    char_stats[template[0]] += 1  # template's first char is not double counted
    char_stats[template[-1]] += 1  # same with last char
    # correct double counting of chars
    char_stats = {c: f // 2 for c, f in char_stats.items()}

    max_freq = max(freq for freq in char_stats.values())
    min_freq = min(freq for freq in char_stats.values())
    print(f"#most common element - #least common element : {max_freq-min_freq}")


if __name__ == "__main__":
    main()
