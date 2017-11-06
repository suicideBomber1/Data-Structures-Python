from pythonds.basic.stack import Stack


def par_checker(symbol):
    s = Stack()
    i = 0
    while i < len(symbol):
        if symbol[i] == '(':
            s.push(symbol[i])
        else:
            if s.isEmpty() != True:
                s.pop()
        i += 1
    if s.isEmpty():
        return True
    else:
        return False


print(par_checker('()()'))
print(par_checker('(()'))
