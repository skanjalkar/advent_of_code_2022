import pry

def read():
    with open("input.in") as f:
        content = f.read().splitlines()
    return content

def operation(operator, right, constant):
    if constant == "old":
        constant = right
    else:
        constant = int(constant)

    if operator == "*":
        left = right * constant
    elif operator == "/":
        left = right / constant
    elif operator == "+":
        left = right + constant
    else:
        left = right - constant
    left = int(left/3)
    return left

def test(right, constant, mondic, current, i, j):
    if right % constant == 0:
        mondic[i][0].append(right)
        return
    else:
        mondic[j][0].append(right)
        return

def part1(mondic, count):
    j = 0
    track = [0]*count
    while j < 20:
        for i in range(count):
            track[i] += len(mondic[i][0])
            for item in mondic[i][0]:
                new_val = operation(mondic[i][1][0], item, mondic[i][1][1])
                test(new_val, mondic[i][2][0], mondic, i, mondic[i][2][1], mondic[i][2][2])

            mondic[i][0] = []

        # pry()
        j += 1

    track.sort(reverse=True)
    print(track[0]*track[1])


def main():
    content = read()
    mondic = {}
    count = 0
    for i in range(0, len(content), 7):
        mondic[count] = []
        items = content[i+1][18:].split(',')
        flag = False
        new_items = []
        for item in items:
            if not flag:
                new_items.append(int(item))
                flag = True
            else:
                new_items.append(int(item[1:]))
        mondic[count].append(new_items)

        operator, constant = content[i+2][23], content[i+2][25:]
        mondic[count].append((operator, constant))

        test_constant = int(content[i+3][21:])
        # print(content[i+4][-1])
        m1, m2 = int(content[i+4][-1]), int(content[i+5][-1])

        mondic[count].append((test_constant, m1, m2))
        count += 1
    # print(mondic)
    part1(mondic, count)

if __name__ == "__main__":
    main()