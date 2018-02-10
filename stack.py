from test import testEqual
from pythonds import Stack


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    s = Stack()
    for ch in mystr:
        s.push(ch)

    revstr = ''
    while not s.is_empty():
        revstr += s.pop()

    return revstr
