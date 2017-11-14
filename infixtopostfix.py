from pythonds.basic.stack import Stack


def infix_to_postfix(k):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    postfix = []
    opstack = Stack()
    token_list = list(k)

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfix.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfix.append(opstack.pop())
    return "".join(postfix)



def validate_input(expr):
    if not expr:
        return False
    expr = expr.strip()
    







# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("2+7*5"))
