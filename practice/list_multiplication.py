# 3/11/2021

# multiply list -> 11 22 33 44 55 66  [odd_list] * [even_list]  

def main():
    number = input()
    array = input().split()
    # print(type(array))
    odd_list = []
    even_list = []
    for i in array:
        # print(type(i))
        if int(i) % 2 == 0:
            even_list.append(int(i))  # [22, 44, 66]
        else:
            odd_list.append(int(i))   # [11, 33, 55]
    even_list = sum(even_list)  # 132
    odd_list = sum(odd_list)    # 99
    output = odd_list * even_list
    print(output)                   

    
    # output -> 13068
