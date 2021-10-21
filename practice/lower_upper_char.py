# 21/10/2021

# find number of lower and upper characters in string

def main():
    text = input()  # I Am Awesome
    # print(text)
    upper_count, lower_count = 0, 0
    for i in range(len(text)):
        # print(text[i])
        if (text[i]).isupper():
            upper_count+= 1
        elif (text[i]).islower():
            lower_count+= 1  
        else:
            pass       
    print(upper_count)
    print(lower_count)
    
    
    # output -> 3 7
