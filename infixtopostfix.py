from pythonds.basic.stack import Stack
from Parenchecker import parenchecker


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
    cp = []
    for e in expr:
        if e == '(' or e == ')':
            cp.append(e)

    parens = ''.join(cp)
    if not parenchecker(parens):
        return False
    tokens = expr.split(" ")
    clean_tokens = []
    for t in tokens:
        t = t.strip()
        clean_tokens.append(t)
        if t.isdigit():
            continue
        elif t == '+' or t == '-' or t == '/' or t == '*' or t == '^':
            continue
        elif t == '(' ot t == ')':
            continue
        else:
            return False
    return clean_tokens


def read_input():
    print("Enter the inflix expression with spaces. ")
    infix = input("infix expression: ")
    ip = validate_input(infix)
    while not ip:
        print("Not a valid expression! Please enter the correct infix input.")
        print("Enter the correct infix expression with space.")
        infix = input("infix expression: ")
    return ip


def main():
    infix = read_input()
    postfix = infix_to_postfix(infix)
    print("Post infix expression is: ", postfix)


# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("2+7*5"))
