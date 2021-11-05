# 5/11/2021

# you need to take number of elements as input on one line and array elements as an input on another line. You need to find the average of even numbers, then the average of odd numbers 
# and add them (round the averages to the nearest integers).

# ip -> 11 22 33 44 55 66

def main():
    size = input()
    array = input().split()
    even_list = []
    odd_list = []
    for i in array:
        if int(i) % 2 == 0:
            even_list.append(int(i))
        else:
            odd_list.append(int(i)) 
    even_average = (sum(even_list)/len(even_list))
    odd_average = (sum(odd_list)/len(odd_list))
    average_sum = int(odd_average + even_average)
    print(average_sum)
    
    
# other approach

import math

def main():
    size = input()
    lst = list(map(int, input().split()))
    o,e, odd, even = 0,0,0,0
    for i in lst:
        if i%2 == 0:
            even+= i
            e+= 1
        else:
            odd+= i
            o+= 1
    if o == 0:
        print(math.ceil(even/e))
    elif e == 0:
        print(math.ceil(odd/o))
    else:
        print(math.ceil((even/e)+(odd/o)))    

        
# op -> 77
