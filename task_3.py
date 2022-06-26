def zeros(n):
    count_5 = n // 5

    pow_5 = 25
    count_pow = 1
    while pow_5 <= n:
        tmp_n = 1
        while pow_5 * tmp_n <= n:
            if tmp_n % 5:
                count_5 += count_pow
            tmp_n += 1
        pow_5 *= 5
        count_pow += 1

    return count_5
