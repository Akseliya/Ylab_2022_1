import itertools


def bananas(s) -> set:
    result = set()
    banana = 'banana'
    if len(s) < len(banana):
        return result

    index_combs = itertools.combinations((i for i in range(len(s))),
                                         len(s) - len(banana))
    for index_comb in index_combs:
        index_comb = set(index_comb)
        banana_i = 0
        new_str = ''
        for i in range(len(s)):
            if i in index_comb:
                new_str += '-'
                continue
            if s[i] != banana[banana_i]:
                break
            new_str += banana[banana_i]
            banana_i += 1
        else:
            result.add(new_str)

    return result
