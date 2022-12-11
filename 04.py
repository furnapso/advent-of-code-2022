def main():
    with open("04_input.txt") as f:
        input = f.read().strip()

    fully_contained_count = 0
    overlap_count = 0

    for line in input.split("\n"):
        vals = line.split(",")
        if either_fully_contained(vals[0], vals[1]):
            fully_contained_count += 1
            overlap_count += 1
        else:
            if overlaps(vals[0], vals[1]):
                overlap_count += 1

    print(f"Part one: {fully_contained_count}")
    print(f"Part two: {overlap_count}")


def either_fully_contained(r1: str, r2: str) -> bool:
    r1_lower, r1_upper = list(map(lambda x: int(x), r1.split("-")))
    r2_lower, r2_upper = list(map(lambda x: int(x), r2.split("-")))

    if r1_lower <= r2_lower and r1_upper >= r2_upper:
        return True
    elif r2_lower <= r1_lower and r2_upper >= r1_upper:
        return True
    else:
        return False


def overlaps(r1: str, r2: str) -> bool:
    r1_lower, r1_upper = list(map(lambda x: int(x), r1.split("-")))
    r2_lower, r2_upper = list(map(lambda x: int(x), r2.split("-")))

    return r1_lower <= r2_upper and r1_upper >= r2_lower


if __name__ == "__main__":
    main()
