with open('2/input.txt') as f:
    directions = f.read().split('\n')
    directions = [(d.split(' ')[0], int(d.split(' ')[1])) for d in directions]


def part_1():
    forward = 0
    depth = 0
    for d, v in directions:
        if d == 'forward':
            forward += v
        elif d == 'down':
            depth += v
        else:
            depth -= v
    return forward * depth

def part_2():
    aim = 0
    forward = 0
    depth = 0
    for d, v in directions:
        if d == 'forward':
            forward += v
            depth += v*aim
        elif d == 'down':
            aim += v
        else:
            aim -= v
    return forward * depth

# print(part_1())
print(part_2())