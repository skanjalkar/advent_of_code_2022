def read():
    with open("input.in") as f:
        content = f.read().splitlines()
    return content


def part1(content):
    curr_head = (0, 0)
    curr_tail = (0, 0)

    for direction in content:
        head_move = direction.split(' ')
        if head_move[0] == "R":
            for i in range(int(head_move[-1])):
                if not reachable(curr_head[0], curr_head[1]+1):



def reachable(hx, hy, tx, ty):
    if abs(hx-tx)>1 and abs(hy-ty)>1:
        return (1, 1)
    elif abs()



def main():
    content = read()
    part1(content)

if __name__ == "__main__":
    main()