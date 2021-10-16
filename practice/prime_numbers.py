# To find prime numbers within an interval

def main():
    low= int(input())
    up = int(input())
    a = set()
    count =0
    for num in range(low, up+1):
    # only numbers >1 are prime in nature
        if (num > 1):
        # factors of numbers to check for prime nature
            for i in range(2,num):
                if( num % i )== 0:
                    break
            else:
                # print(num)
                a.add(num)
                count +=1

    # print(a)
    print(count)
