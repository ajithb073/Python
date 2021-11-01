# 1/11/2021

# ip -> 100   op -> 4


def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10    # 0, 0 , 1 
        decimal = decimal + dec * pow(2, i)  # 0, 0, 4
        binary = binary//10   # 10, 1 
        i += 1  # 0, 1, 2
    print(decimal)
    
    
 # inbuilt  int(binary_number, 2)



# decimal to binary  bin(decimal_number)
