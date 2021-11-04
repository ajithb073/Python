# 4/11/2021

# max and min multiplication

# ip -> 11 22 33 44 55 66

def main():
    size = input()
    array = input().split()
    array = sorted(array)
    # print(array)
    least_value = int(array[0])  # least value - 11
    high_value = int(array[-1])   # high value - 66
    # print(least_value, high_value)
    output = least_value * high_value
    print(output)


# op -> 726
