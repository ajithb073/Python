# 2/11/2021

# add odd index and even index elemnt and subtract it

# ip -> 11 22 33 44 55 66

def main():
    number = input()
    array = input().split()
    # print(array)
    odd_list = []
    even_list = []
    for idx, elem in enumerate(array):
        if idx % 2 == 0:
            even_list.append(int(elem)) #[11, 33, 55]
        else:
            odd_list.append(int(elem))  #[22, 44, 66] 
    even_list = sum(even_list)  # 99
    odd_list = sum(odd_list)    # 132
    # print(even_list, odd_list) 
    output = odd_list - even_list  # 33
    print(output)

 # op -> 33 [132 -99]   
