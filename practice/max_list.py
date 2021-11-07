# 7/11/2021

# ip -> 345678
# op -> 8

def main():
    # inp = list(map(int, input().split()))
    inp = input()
    lst = []
    for i in range(len(inp)):
        lst.append(int(inp[i]))
    # print(lst)
    max_elem = max(lst)
    print(max_elem) 
