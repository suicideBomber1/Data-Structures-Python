def jugs_counts(v1, v2, water):
	
    pass


def diophantine(v1, v2, water):
    a = 0
    result = []
    while a >= 0:
        b = (water - (v1 * a)) // v2
        if (water - (v1 * a)) % v2 == 0:
            break
        else:
            a += 1
    result.append([a, b])

    a = 0
    while a <= 0:
        b = (water - (v1 * a)) // v2
        if (water - (v1 * a)) % v2 == 0:
            break
        else:
            a -= 1
    result.append([a, b])

    return result


print(diophantine(4, 3, 2))
