from pythonds.basic.stack import Stack


def postfix_eval(p):
    opdstack = Stack()
    token_list = p.split()

    for token in token_list:
        if token in '0123456789':
            opdstack.push(int(token))
        else:
            opd1 = opdstack.pop()
            opd2 = opdstack.pop()
            result = do_math(token, opd1, opd2)
            opdstack.push(result)

    return opdstack.pop()


def do_math(op, opd1, opd2):
    if op == '*':
        return opd1 * opd2
    elif op == '/':
        return opd1 / opd2
    elif op == '+':
        return opd1 + opd2
    elif op == '-':
        return opd1 - opd2


print(postfix_eval('7 8 + 3 2 + /'))
