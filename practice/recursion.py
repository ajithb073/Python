# 26/10/2021

# two integers from user ( base number and a exponent) and calculates the power using recursion

# input -> 4 3; output -> 4^3 = 4*4*4 = 64 




def power(a,b):
  if (b == 0):
    return 1
  else:
    return (a*power(a, b-1))

def main():
  i = list(map(int, input().split()))
  ans = power(i[0], i[1])
  print(ans, end = "")
