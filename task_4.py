import itertools


def bananas(s) -> set:
    result = set()
    banana = 'banana'
    if len(s) < len(banana):
        return result

    # составление бинарных комбинаций
    combs = []
    i = 63  # '0b111111'
    bin_str = bin(i)[2:]
    while len(bin_str) <= len(s):
        if bin_str.count('1') == len(banana):
            new_comb = '0' * (len(s) - len(bin_str)) + bin_str
            combs.append(tuple(bool(int(x)) for x in new_comb))
        i += 1
        bin_str = bin(i)[2:]

    for comb in combs:
        if ''.join(itertools.compress(s, comb)) != banana:
            continue
        new_str = ''.join(s[i] if comb[i] else '-' for i in range(len(s)))
        result.add(new_str)

    return result
