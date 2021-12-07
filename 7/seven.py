with open('7/input.txt') as f:
    positions = list(map(int, f.read().split(',')))


def min_fuel(fn):
    min_fuel = None
    for i in range(max(positions)+1):
        fuel = sum(fn(pos-i) for pos in positions)
        if min_fuel is None:
            min_fuel = fuel
        else:
            min_fuel = min(fuel, min_fuel)
    return min_fuel


def part_1():
    return min_fuel(abs)

def part_2():
    def sum_to_n(n):
        n = abs(n)
        return n * (n + 1) // 2
    return min_fuel(sum_to_n)

print(part_1())
print(part_2())
