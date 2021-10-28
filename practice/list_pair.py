# 28/10/2021

# join pair of list and check if the match     Print 'True' if the pair found in the array element else print 'False' to the stdout. 
#7
# 33 12 -76 11 9 7 6
# 20


def main():
    array_size = int(input())
    # print(array_size)
    array = input()
    array = array.split(" ")
    # array = ast.literal_eval(array)
    # print(type(array))
    pair = int(input())
    # print(pair)
    all_pair_values = []
    for previous, current in zip(array, array[1:]):
        # print(previous, current)
        values = (int(previous)+int(current))
        all_pair_values.append(values)
    if pair in all_pair_values:
        print("True") 
    else:
        print("False") 
            
            
 # 11 + 9 -> 20 True           
