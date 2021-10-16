# Program to check if a number is prime or not

num = 999

# prime numbers are greater than 1
if num > 1:
   # check for factors
    for i in range(2,num):
#         print(i)
        # no factors should be divisible by number
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(i)
        print(num,"is a prime number")
       
# if input number is less than or equal to 1, it is not prime
else:
    print("final else:",num,"is not a prime number")
    
# 999 is not a prime number
# 3 times 333 is 999
    
