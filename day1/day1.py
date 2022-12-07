def main():
    with open('sample.in') as f:
        content = [n.strip() for n in f.readlines()]
        elves = []
        cur = 0
        count = 1

        for line in content:
            if line == '':
                elves.append(cur)
                cur = 0
            else:
                cur += int(line)
        elves.append(cur)

        print(max(elves)) # part one
        print(sum(sorted(elves, reverse=True)[:3])) # part two


if __name__ == "__main__":
    main()