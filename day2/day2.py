def part1(content):
    rules = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
    ans = 0
    for i, round in enumerate(content):
        ans += rules[f'{round[0]}{round[2]}']
    print(ans)

def part2(content):
    rules = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    ans = 0
    for i, round in enumerate(content):
        ans += rules[f'{round[0]}{round[2]}']
    print(ans)



def main():
    with open("input.in") as f:
        content = f.readlines()
    part1(content)
    part2(content)


if __name__ == "__main__":
    main()