def part1(content):
    ans = 0
    for j, rucksacks in enumerate(content):
        rucksack1 = set(rucksacks[:len(rucksacks)//2])
        rucksack2 = set(rucksacks[len(rucksacks)//2:])

        chr = list(rucksack1.intersection(rucksack2))
        if len(chr)==0:
            continue
        if ord(chr[0])>=97 and ord(chr[0])<=122:
            ans += ord(chr[0])-96
        else:
            ans += ord(chr[0])-38

    print(ans)

def part2(content):
    ans = 0
    for i in range(0, len(content),3):
        key1 = set(content[i][:len(content[i])-1])
        key2 = set(content[i+1][:len(content[i+1])-1])
        key3 = set(content[i+2][:len(content[i+2])-1])

        chr = list(key1.intersection(key2.intersection(key3)))

        if ord(chr[0])>=97 and ord(chr[0])<=122:
            ans += ord(chr[0])-96
        else:
            ans += ord(chr[0])-38
    print(ans)


def main():
    with open("input.in") as f:
        content = f.readlines()
    part1(content)
    part2(content)



if __name__ == "__main__":
    main()