def part1(content):
    ans = 0
    for assignment in content:
        test = []
        tmp = ""
        for num in assignment:
            if num == "-" or num == ",":
                test.append(tmp)
                tmp = ""
            else:
                tmp += num
        test.append(tmp)
        first = set(range(int(test[0]), int(test[1])+1))
        second = set(range(int(test[2]), int(test[3])+1))

        if first.issubset(second) or second.issubset(first):
            ans += 1

    print(ans)

def part2(content):
    ans = 0
    for assignment in content:
        test = []
        tmp = ""
        for num in assignment:
            if num == "-" or num == ",":
                test.append(tmp)
                tmp = ""
            else:
                tmp += num
        test.append(tmp)

        first = set(range(int(test[0]), int(test[1])+1))
        second = set(range(int(test[2]), int(test[3])+1))

        if first & second:
            ans += 1
    print(ans)

def main():
    with open("input.in") as f:
        content = f.read().splitlines()

    part1(content)
    part2(content)

if __name__ == "__main__":
    main()