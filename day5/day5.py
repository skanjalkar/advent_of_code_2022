import pry

def read():
    with open("input.in") as f:
        content = f.read().splitlines()

    return content


def part1(content):
    crates = {}
    read = False
    lanes = 1
    for k, info in enumerate(content):
        if info == "":
            for key in crates:
                crates[key] = crates[key][::-1]
            continue
        if not read:
            if info[1] == "1":
                read = True
                continue
            count = 1
            for i in range(1, len(info), 4):
                if info[i] == " ":
                    count += 1
                    continue
                if str(count) not in crates:
                    crates[str(count)] = [info[i]]
                else:
                    crates[str(count)].append(info[i])
                count += 1
            lanes = max(lanes, count)
        else:
            move = info.split(' ')
            for i in range(int(move[1])):
                transfer = crates[move[3]].pop()
                crates[move[-1]].append(transfer)
    ans = ""
    for i in range(1, lanes):
        ans += crates[str(i)][-1]
    print(ans)


def part2(content):
    crates = {}
    read = False
    lanes = 1
    for k, info in enumerate(content):
        if info == "":
            for key in crates:
                crates[key] = crates[key][::-1]
            continue
        if not read:
            if info[1] == "1":
                read = True
                continue
            count = 1
            for i in range(1, len(info), 4):
                if info[i] == " ":
                    count += 1
                    continue
                if str(count) not in crates:
                    crates[str(count)] = [info[i]]
                else:
                    crates[str(count)].append(info[i])
                count += 1
            lanes = max(lanes, count)
        else:
            move = info.split(' ')
            temp = []
            for i in range(int(move[1])):
                transfer = crates[move[3]].pop()
                temp.append(transfer)
            temp = temp[::-1]
            crates[move[-1]] += temp

    ans = ""
    for i in range(1, lanes):
        ans += crates[str(i)][-1]
    print(ans)


def main():
    content = read()
    part1(content)
    part2(content)

if __name__ == "__main__":
    main()