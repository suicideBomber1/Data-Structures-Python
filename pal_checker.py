from pythonds.basic.deque import Deque


def pal_checker(string):
    d = Deque()
    for ch in string:
        d.addRear(ch)

    result = True

    while d.size() > 1 and result:
		first = d.removeFront()
	    last = d.removeLast()
	    while first != last:
	    	result = False

    return result

print(palchecker("lsdkjfskf"))


