from pythonds.basic.stack import Stack

s = Stack()


def divideby2(dec_num):
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2

    binnum = ''
    while not s.isEmpty():
        binnum += str(s.pop())

    return binnum


print(divideby2(42))
