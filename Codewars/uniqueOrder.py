def unique_in_order(iterable):
    order = list(iterable)
    uniq =[]
    length = len(order)
    if len(order) == 0:
        return []
    else:
        for i in range(1, len(order)-1):
            if order[i] != order[i + 1]:
                uniq.append(order[i])
        uniq.append(order[-1])
        return uniq
    



print(unique_in_order('AAAABBBCCDAABBB'))