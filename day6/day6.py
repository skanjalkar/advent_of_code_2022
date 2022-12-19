def read():
    with open("input.in") as f:
        content = f.read()
    return content

def part1(content):
    for i in range(len(content)-4):
        # print(set(content[i:i+4]))
        if len(set(content[i:i+4])) == 4:
            return i+4

def part2(content):
    for i in range(len(content)-14):
        # print(set(content[i:i+4]))
        if len(set(content[i:i+14])) == 14:
            return i+14

def main():
    content = read()
    ans = part1(content)
    print(ans)
    print(part2(content))

if __name__ == "__main__":
    main()