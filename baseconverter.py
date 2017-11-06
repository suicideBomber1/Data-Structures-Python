from pythonds.basic.stack import Stack


def base_converter(dec_num, base):
    s = Stack()
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while dec_num > 0:
        rem = dec_num % base
        s.push(rem)
        dec_num = dec_num // base

    conv_str = ''
    while not s.isEmpty():
        conv_str += digits[s.pop()]

    return conv_str


print(base_converter(26, 26))
