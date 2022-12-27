import pry
def read():
    with open('input.in') as f:
        content = f.read().splitlines()
    return content

def part1(content):
    sum_x = 0
    cycle_sum = 1
    cycle = [20, 60, 100, 140, 180, 220]
    count = 0
    seperate_counter = 0
    for i, instruction in enumerate(content):
        split = instruction.split(" ")
        if split[0] == "addx":
            seperate_counter += 1
            if seperate_counter == cycle[count]:
                print(count)
                sum_x += seperate_counter * cycle_sum
                count += 1
                if count == len(cycle):
                    return sum_x


            seperate_counter += 1
            cycle_sum += int(split[-1])
            if seperate_counter == cycle[count]:
                print(count)
                sum_x += seperate_counter * cycle_sum
                count += 1

                if count == len(cycle):
                    return sum_x
        else:
            seperate_counter += 1
            if seperate_counter == cycle[count]:
                sum_x += seperate_counter * cycle_sum
                count += 1
                if count == len(cycle):
                    return sum_x

        # print(cycle_sum, seperate_counter, "DEBUG")
    return sum_x

def part2(content):
    pass

def main():
    content = read()
    print(part1(content))

if __name__ == "__main__":
    main()