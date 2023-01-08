import json
import pry

def read():
    with open("input.in", "r") as f:
        content = f.read().splitlines()
    return content

def compare(list1, list2):
    i, j = 0, 0
    while i<len(list1) and j<len(list2):
        if type(list1[i]) == int and type(list2[j]) == int:
            if list1[i]>list2[j]:
                return False
        elif type(list1[i]) == int and type(list2[j]) == list:
            if list1[i] - list2[j][0] > 0:
                return False
        else:
            k, l = 0, 0

        i+=1
        j+=1

def part1(content):
    for i in range(0, len(content), 3):
        list1 = json.loads(content[i])
        list2 = json.loads(content[i+1])
        pry()



def main():
    content = read()
    part1(content)


if __name__ == "__main__":
    main()