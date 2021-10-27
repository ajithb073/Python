# 27/10/2021

# gcd/hcf of two numbers  -> [largest positive integer that perfectly divides the two given numbers]


# ip -> 81 81

import math

def main():
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    output = math.gcd(a,b)
    print(output)
    
# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):  #(1,25)
        if((x % i == 0) and (y % i == 0)):   # and condition satifies, that will be hcf value
            hcf = i 
    return hcf    
    
# op -> 81    
