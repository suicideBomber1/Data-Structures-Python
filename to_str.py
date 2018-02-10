def to_str(n, base):
    conv_str = "0123456789ABCDEF"
    if n < base:
        return conv_str[n]
    else:
        return to_str(n // base, base) + conv_str[n % base]


print(to_str(1453, 16))
