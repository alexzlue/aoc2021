import collections

with open('8/input.txt') as f:
    numbers = f.read().split('\n')
    numbers = [n.split(' | ') for n in numbers]
    get_letter_sets = lambda strings: [frozenset(group) for group in strings.split(' ')]
    numbers = [[get_letter_sets(nums), get_letter_sets(questions)] for nums, questions in numbers]

class SevenSegmentNumbers:
    num_to_ssn = [None for i in range(10)]
    uniques = {2: 1, 3: 7, 4: 4, 7: 8}
    e = None

    def __init__(self, numbers):
        self.num_seg_to_sets = collections.defaultdict(list)
        for number in numbers:
            if len(number) in self.uniques:
                self.num_to_ssn[self.uniques[len(number)]] = number
            else:
                self.num_seg_to_sets[len(number)].append(number)

    def _solve_5ssns(self):
        four = self.num_to_ssn[4]
        seven = self.num_to_ssn[7]
        eg = None
        g = None
        for segments in self.num_seg_to_sets[5]:
            diff = segments - seven - four
            if len(diff) == 2:
                eg = diff
                self.num_to_ssn[2] = segments
                continue
            g = diff
            if seven.issubset(segments):
                self.num_to_ssn[3] = segments
            else:
                self.num_to_ssn[5] = segments
        self.e = eg - g

    def _solve_6ssns(self):
        seven = self.num_to_ssn[7]
        for segments in self.num_seg_to_sets[6]:
            if not seven.issubset(segments):
                self.num_to_ssn[6] = segments
                continue
            if self.e.issubset(segments):
                self.num_to_ssn[0] = segments
            else:
                self.num_to_ssn[9] = segments


    def solve(self):
        self._solve_5ssns()
        self._solve_6ssns()

    def decode_ssn_num(self, code):
        code_to_num = {ssn: str(i) for i, ssn in enumerate(self.num_to_ssn)}
        decoded = [code_to_num[ssn] for ssn in code]
        return int(''.join(decoded), 10)


def part_1():
    total_uniques = 0
    ssn_nums = [ssn for ssns in numbers for ssn in ssns[1]]
    for ssn_num in ssn_nums:
        if len(ssn_num) in SevenSegmentNumbers.uniques:
            total_uniques += 1
    return total_uniques

def part_2():
    decoded_nums = []
    for number, code in numbers:
        ssn = SevenSegmentNumbers(number)
        ssn.solve()
        decoded_nums.append(ssn.decode_ssn_num(code))

    return sum(decoded_nums)

print(part_1())
print(part_2())
