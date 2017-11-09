from pythonds.basic.queue import Queue


def hot_potato(names, num):
    s = Queue()
    for name in names:
        s.enqueue(name)

    while s.size() > 1:
        for i in range(num):
            s.enqueue(s.dequeue())
        s.dequeue()

    return s.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
