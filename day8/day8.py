def read():
    with open("input.in") as f:
        content = f.read().splitlines()
    new_content = []
    for c in content:
        c = list(c)
        temp = []
        for i in c:
            temp.append(int(i))
        new_content.append(temp)
    return new_content

def part1(content):
    ans = 0
    for i in range(len(content)):
        for j in range(len(content[0])):
            if is_visible(content, i, j):
                ans += 1
    return ans

def part2(content):
    ans = 1
    for i in range(len(content)):
        for j in range(len(content[0])):
            ans = max(ans, best_score(content, i, j))
    return ans


def best_score(content, i, j):
    top, left, right, bot = 0, 0, 0, 0
    # go top
    x, y = i, j

    while isLegal(content, x-1, y):
        if content[x-1][y]>=content[i][j]:
            top += 1
            break
        top += 1
        x -=1

    x, y = i, j
    while isLegal(content, x, y-1):
        if content[x][y-1]>=content[i][j]:
            left += 1
            break
        y -= 1
        left += 1

    # go left
    x, y = i, j
    while isLegal(content, x, y+1):
        if content[x][y+1]>=content[i][j]:
            right += 1
            break
        y += 1
        right += 1
    x, y = i, j

    while isLegal(content, x+1, y):
        if content[x+1][y] >= content[i][j]:
            bot += 1
            break
        x += 1
        bot += 1

    return top*bot*left*right


def is_visible(content, i, j):
    flag_top = True
    flag_bot = True
    flag_left = True
    flag_right = True
    # go top
    x, y = i, j
    while isLegal(content, x-1, y):
        if content[x-1][y]>=content[i][j]:
            flag_top = False
            break
        x -=1
    if flag_top:
        return True

    x, y = i, j
    while isLegal(content, x, y-1):
        if content[x][y-1]>=content[i][j]:
            flag_left = False
            break
        y -= 1
    if flag_left:
        return True
    # go left
    x, y = i, j
    while isLegal(content, x, y+1):
        if content[x][y+1]>=content[i][j]:
            flag_right = False
            break
        y += 1

    if flag_right:
        return True

    x, y = i, j

    while isLegal(content, x+1, y):
        if content[x+1][y] >= content[i][j]:
            flag_bot = False
            break
        x += 1

    if flag_bot:
        return True

    return False
    # go right
    # go bottom

def isLegal(content, i, j):
    if i<0 or i>=len(content) or j<0 or j>=len(content[0]):
        return False
    return True

def main():
    content = read()
    print(part1(content))
    print(part2(content))

if __name__ == "__main__":
    main()