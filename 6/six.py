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

    def val(self):
        return self.state

def part_1():
    fishes = [Fish(state) for state in states]
    for _ in range(80):
        new_fishes = []
        for fish in fishes:
            new = fish.process_new_day()
            if new:
                new_fishes.append(new)
        fishes += new_fishes
    return len(fishes)

def part_2():
    fishes = collections.Counter(states)
    for _ in range(256):
        next_day_fishes = collections.defaultdict(int, {
            state-1: count for state, count in fishes.items() if state-1 >= 0
        })
        if 0 in fishes:
            next_day_fishes[8] += fishes[0]
            next_day_fishes[6] += fishes[0]
        fishes = next_day_fishes
    return sum(fishes.values())

print(part_1())
print(part_2())
