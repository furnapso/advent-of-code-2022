def main():
    with open("01_input.txt") as f:
        input = f.read()

    elves = input.split("\n\n")
    elf_totals = []

    for elf in elves:
        elf_totals.append(get_reindeer_total(elf))

    print(f"Part one: {max(elf_totals)}")

    sorted_elf_totals = sorted(elf_totals, reverse=True)
    print(f"Part two: {sum(sorted_elf_totals[:3])}")


def get_reindeer_total(elf: list) -> int:
    vals = [int(i) for i in elf.split("\n") if i != '']
    return sum(vals)


if __name__ == "__main__":
    main()
