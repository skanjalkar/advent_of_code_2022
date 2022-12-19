class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.memory = 0
        self.children = []

def read():
    with open("input.in") as f:
        content = f.read().splitlines()
    return content

def pre_order():
    pass

def part1(content):
    print(content)

def main():
    content = read()
    part1(content)

if __name__ == "__main__":
    main()