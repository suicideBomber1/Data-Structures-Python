from pythonds.basic.stack import Stack
<<<<<<< HEAD


def infix_to_postfix(k):
	prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    postfix = []
    opstack = Stack()
    token_list = k.split()

    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or '0123456789':
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = opstack.pop()
        else:
            while not opstack.isEmpty() and prec[opstack.peek()] >= prec[token]:
                postfix.append(opstack.pop())
            token_list.push()

        while not opstack.isEmpty():
            postfix.append(opstack.pop())
        return ''.join(postfix)


print(infix_to_postfix("A * B + C * D"))
=======
>>>>>>> 3e1d66f242d62dc3fc32f7a567a73d43afe915df
