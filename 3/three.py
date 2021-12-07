import collections

with open('3/input.txt') as f:
    report = f.read().split('\n')


class Node:

    def __init__(self, bit):
        self.bit = bit
        self.occs = 1
        self.bins = {'0': None, '1': None}


class Trie:

    def __init__(self):
        self.head = Node('b')
        self.bin_len = None

    def add_binary(self, binary):
        node = self.head
        self.bin_len = len(binary) if self.bin_len is None else self.bin_len
        for bin in binary:
            if not node.bins[bin]:
                node.bins[bin] = Node(bin)
            else:
                node.bins[bin].occs += 1
            node = node.bins[bin]

    def get_leaf_binary(self, is_o):
        node = self.head
        binary_list = []
        for _ in range(self.bin_len):
            if any(bin is None for bin in node.bins.values()):
                bit, bin_node = [(v, n) for v, n in node.bins.items() if n is not None][0]
                binary_list.append(bit)
                node = bin_node
                continue
            mc_bits = collections.Counter({bit: node.occs for bit, node in node.bins.items()}).most_common()
            if mc_bits[0][1] > mc_bits[1][1]:
                bit = mc_bits[0][0] if is_o else mc_bits[1][0]
            else:
                bit = '1' if is_o else '0'
            binary_list.append(bit)
            node = node.bins[bit]
        return ''.join(binary_list)
            


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

def part_2_trie():
    trie = Trie()
    for binary in report:
        trie.add_binary(binary)
    o2_val = trie.get_leaf_binary(True)
    co2_val = trie.get_leaf_binary(False)

    return int(o2_val, 2) * int(co2_val, 2)

print(part_1())
print(part_2())
print(part_2_trie())