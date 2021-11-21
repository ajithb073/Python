# 10 2 3
# 3 1
# 5 2 8

# op -> 9  Buy the keyboard and the USB drive for a total cost of 9


# 5 1 1
# 4
# 5

# op -> -1

def getMoneySpent(keyboards, drives, b):
    item_list = [-1]
    keyboards = sorted(keyboards)
    for i in keyboards:
        # print("i",i)
        for j in drives:
            # print("j", j)
            if (i+j <= b):
                kb_dr = i + j
                item_list.append(kb_dr)
    return max(item_list)
