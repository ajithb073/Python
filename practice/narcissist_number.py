# 19/10/2021
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 -> square of total length

number = input()
sum_value = 0
total_len = len(number)
# print(total_len)
number = int(number)
# print(type(number))
temp = number
while temp > 0:
    digit = temp % 10
    sum_value += digit ** total_len
    temp = temp // 10
    # print(sum_value)
    # print("*********")
if (number == sum_value):
    print("True")
else:
    print("False") 
