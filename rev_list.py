def rev_list(alist):
    if len(alist) == 1:
        return alist
    else:
        return rev_list(alist[1:]) + [alist[0]]


print(rev_list([1, 2, 3, 4]))
