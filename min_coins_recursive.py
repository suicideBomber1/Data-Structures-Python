def rec_mc(coin_list, change):
    min_coins = change
    if change in coin_list:
        return 1
    else:
        for i in [c for c in coin_list if c <= change]:
            num_coins = 1 + rec_mc(coin_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


## Memoized solution ## Cached Solution ##

def rec_mc(coin_list, change, known_results):
    min_coins = change
    if change in coin_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_list if c <= change]:
            num_coins = 1 + rec_mc(coin_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


print(rec_mc([1, 5, 10, 25], 63, [0] * 64))
