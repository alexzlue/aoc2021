import collections

with open('6/input.txt') as f:
    states = list(map(int, f.read().split(',')))

class Fish:

    def __init__(self, state):
        self.state = state
    
    def process_new_day(self):
        self.state -= 1
        if self.state == -1:
            self.state += 7
            return Fish(8)
        return None

def get_fishes_brute(days):
    fishes = [Fish(state) for state in states]
    for _ in range(days):
        new_fishes = []
        for fish in fishes:
            new = fish.process_new_day()
            if new:
                new_fishes.append(new)
        fishes += new_fishes
    return len(fishes)

def get_fishes(days):
    fishes = collections.Counter(states)
    for _ in range(days):
        next_day_fishes = collections.defaultdict(int, {
            state-1: count for state, count in fishes.items() if state-1 >= 0
        })
        if 0 in fishes:
            next_day_fishes[8] += fishes[0]
            next_day_fishes[6] += fishes[0]
        fishes = next_day_fishes
    return sum(fishes.values())

def part_1():
    return get_fishes(80)

def part_2():
    return get_fishes(256)

print(part_1())
print(part_2())
