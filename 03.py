def main():
    with open("03_input.txt") as f:
        input = f.read().strip()

    total = 0

    for line in input.split("\n"):
        compartments = split_midway(line)
        item = is_in_both(compartments[0], compartments[1])
        priority = get_priority(item)
        total += priority

    print(f"Part one: {total}")

    groups = get_groups(input)

    group_priorities = get_group_priorities(groups)

    print(f"Part two: {sum(group_priorities.values())}")


def split_midway(rucksack: str) -> list:
    midway = round(len(rucksack)/2)
    return [rucksack[:midway], rucksack[midway:]]


def is_in_both(c1: str, c2: str) -> str:
    for i in c1:
        if i in c2:
            return i


def get_priority(item: str) -> int:
    priority_index = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return priority_index.index(item)


def is_in_three(r1: str, r2: str, r3: str) -> str:
    for i in r1:
        if i in r2 and i in r3:
            return i


def get_groups(input: str) -> dict:
    count = 0
    group = 1
    groups = {}

    for line in input.split("\n"):
        if count == 3:
            group += 1
            count = 0

        if group not in groups.keys():
            groups[group] = []

        groups[group].append(line)
        count += 1

    return groups


def get_group_priorities(groups: dict) -> dict:
    group_priorities = {}

    for key, val in groups.items():
        letter = is_in_three(val[0], val[1], val[2])
        group_priorities[key] = get_priority(letter)

    return group_priorities


if __name__ == "__main__":
    main()
