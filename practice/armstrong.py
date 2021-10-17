#17/10/2021
#Check number is armstrong or not -> 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

num = int(input())
sum_value = 0
temp = num
while temp >0:
    digit = temp % 10
#     print(digit)
    sum_value+= digit ** 3
#     print(sum_value)
    temp //= 10  #floor division
#     print(temp)
#     print("*******")
if num == sum_value:
    print("True")
else:
    print("False")
    
    
# input -> 370
# 0
# 0
# 37
# *******
# 7
# 343
# 3
# *******
# 3
# 370
# 0
# *******
# 370 is an Armstrong number    
