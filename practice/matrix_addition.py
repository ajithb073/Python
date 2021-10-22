#add two matrices 
# 33  format
# 123
# 456
# 789
# 33
# 123
# 456
# 789


def main():
    a=input().split()
    n=int(a[0])
    m=int(a[1])
    mat1=[]
    for i in range(n):
        row=[]
        row=input().split()
        mat1.append(row)
    b=(input().split())
    p=int(a[0])
    q=int(a[1])
    mat2=[]
    for i in range(p):
        row=[]
        row=input().split()
        mat2.append(row)
    for i in range(0,p):
        # print("i",i)
        for j in range(0,q):
            # print("j",j)
            k=(int(mat1[i][j])+int(mat2[i][j]))
            if i==(p-1) and j==(q-1):
                print(k,end="")
            elif j==(q-1):
                print(k)
            else:
                print(k,end=' ')  
                
             
            
#  i 0
# j 0
# 3 j 1
# 5 j 2
# 7
# i 1
# j 0
# 9 j 1
# 11 j 2
# 13
# i 2
# j 0
# 14 j 1
# 16 j 2
# 18
