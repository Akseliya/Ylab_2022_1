def zeros(n):
    count_5 = n // 5
    pow_5 = 25
    while pow_5 <= n:
        tmp_n = 1
        count_5 += n // pow_5
        pow_5 *= 5

    return count_5
