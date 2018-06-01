from pythonds.basic.deque import Deque


def pal_checker(string):
    d = Deque()
    for ch in string:
        d.addRear(ch)

    result = True
<<<<<<< HEAD

=======
>>>>>>> 3e1d66f242d62dc3fc32f7a567a73d43afe915df
    while d.size() > 1 and result:
		first = d.removeFront()
	    last = d.removeLast()
	    while first != last:
	    	result = False

    return result

print(palchecker("lsdkjfskf"))


