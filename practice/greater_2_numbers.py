# 8/11/2021

# ip -> 345678   444444   op-> 345678
# ip -> 444444   444444   op-> 'Equal'

def main():
    inp = list(map(int, input().split()))
    # print(inp)
    a = inp[0]
    b = inp[1]
    # print(a,b)
    a_sum = sum(int(digit) for digit in str(a))
    b_sum = sum(int(digit) for digit in str(b))
    if a_sum > b_sum:
        # max_sum = max(a_sum, b_sum)
        print(a)
    elif b_sum > a_sum:
        print(b)    
    else:
        print("Equal")
