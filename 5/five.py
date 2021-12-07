import collections

with open('5/input.txt') as f:
    lines = f.read().split('\n')
    line_segments = [line.split(' -> ') for line in lines]
    line_segments = [[tuple(map(int, seg[0].split(','))), tuple(map(int, seg[1].split(',')))] for seg in line_segments]

def get_intersections(use_diagonals=False):
    intersections = collections.Counter()
    for (x1, y1), (x2, y2) in line_segments:
        line = []
        if x1 == x2:
            incr = range(y1, y2+1) if y2 > y1 else range(y2, y1+1)
            for i in incr:
                line.append((x1, i))
        elif y1==y2:
            incr = range(x1, x2+1) if x2 > x1 else range(x2, x1+1)
            for i in incr:
                line.append((i, y1))
        elif use_diagonals:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            if y1 < y2:
                for i in range(0, y2-y1+1):
                    line.append((x1+i, y1+i))
            else:
                for i in range(0, y2-y1-1, -1):
                    line.append((x1-i, y1+i))
        intersections.update(line)
    gte_2 = 0
    for _, i in intersections.items():
        if i >= 2:
            gte_2 += 1
    return gte_2

def part_1():
    return get_intersections()

def part_2():
    return get_intersections(use_diagonals=True)

print(part_1())
print(part_2())
