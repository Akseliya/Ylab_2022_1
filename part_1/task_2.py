def int32_to_ip(int32):
    ipv4 = ''
    for i in range(3):
        ipv4 = '.' + str(int32 % 256) + ipv4
        int32 //= 256
    ipv4 = str(int32) + ipv4

    return ipv4
