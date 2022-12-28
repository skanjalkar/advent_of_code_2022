from collections import deque

def read():
    with open('input.in', 'r') as f:
        content = f.read().splitlines()
    return content

def isValid(i, j, grid):
    if 0<=i<len(grid) and 0<=j<len(grid[0]):
        return True
    return False

def part1(start, grid, goal):
    parent = {}
    parent[start] = None

    neighbours = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    queue = deque()
    queue.append((start[0], start[1], grid[start[0]][start[1]]))
    seen = set()
    seen.add(start)
    while queue:
        i, j, val = queue.popleft()
        if val == goal:
            ans = 0
            while parent[(i, j)] is not None:
                ans += 1
                (i, j) = parent[(i, j)]
            return ans

        for x, y in neighbours:
            if isValid(i+x, j+y, grid) and (i+x, j+y) not in seen:
                if grid[i+x][j+y] - grid[i][j] <= 1:
                    parent[(i+x, j+y)] = (i, j)
                    seen.add((i+x, j+y))
                    queue.append((i+x, j+y, grid[i+x][j+y]))




def main():
    content = read()
    grid = [[None for j in range(len(content[0]))] for i in range(len(content))]
    for i, val in enumerate(content):
        for j, char in enumerate(val):
            if char == "S":
                grid[i][j] = ord("a")-1
                start = (i, j)
            elif char == "E":
                grid[i][j] = ord("z")+1
            else:
                grid[i][j] = ord(char)

    print(part1(start, grid, ord("z")+1))

if __name__ == "__main__":
    main()