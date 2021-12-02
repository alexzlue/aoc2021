with open('1/input.txt') as f:
    depths = f.read().split('\n')
    depths = [int(depth) for depth in depths]

def depth_comparison(win):
    increased = 0
    for i in range(win, len(depths)):
        if depths[i-win] < depths[i]:
            increased += 1
    return increased

def part_1():
    return depth_comparison(1)


def part_2():
    return depth_comparison(3)

print(part_1())
print(part_2())