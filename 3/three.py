import collections

with open('3/input.txt') as f:
    report = f.read().split('\n')


def part_1():
    gamma = []
    epsilon = []

    for bits in list(zip(*report)):
        bits = collections.Counter(bits).most_common()
        gamma.append(bits[0][0])
        epsilon.append(bits[1][0])

    gamma_v = int(''.join(gamma), 2)
    epsilon_v = int(''.join(epsilon), 2)
    return gamma_v * epsilon_v

def part_2():
    def get_updated_vals(vals, i, is_o):
        if len(vals) <= 1:
            return vals
        mc_bits = collections.Counter(bit[i] for bit in vals).most_common()
        if mc_bits[0][1] > mc_bits[1][1]:
            bit = mc_bits[0][0] if is_o else mc_bits[1][0]
        else:
            bit = '1' if is_o else '0'
        return [val for val in vals if val[i] == bit]

    o2_vals = report
    co2_vals = report
    for i in range(len(report[0])):
        o2_vals = get_updated_vals(o2_vals, i, True)
        co2_vals = get_updated_vals(co2_vals, i, False)

    return int(o2_vals[0], 2) * int(co2_vals[0], 2)

print(part_1())
print(part_2())