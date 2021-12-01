with open('1/input.txt') as f:
    depths = f.read().split('\n')
    depths = [int(depth) for depth in depths]


def part_1():
    increased = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            increased += 1
    return increased


def part_2():
    increased = 0
    for i in range(3, len(depths)):
        if depths[i-3] < depths[i]:
            increased += 1
    return increased

print(part_1())
print(part_2())