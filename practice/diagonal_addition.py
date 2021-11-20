
For this challenge, you need to take a matrix as an input from the stdin , calculate the sum of the digits for each diagonal and compare them.For example,
in the below matrix
1 2 3
4 5 6
7 8 9
Diagonal 1 is 1,5,9.
Diagonal 2 is 3,5,7.




def main():
    row, col = map(int, input().split())
    mat = []
    for i in range(row):
        mat.append(input().split())
    # mat = ast.literal_eval(mat)    
    # print(mat)
    dig1, dig2 = 0,0
    for i in range(0, row):
        for j in range(0, col):
            if i==j:
                dig1+=int(mat[i][j])
    for i in range(0, row):
        dig2+=int(mat[i][col-i-1]) 
    if dig1 > dig2:
        print('Diagonal 1')
    elif dig2 > dig1:
        print('Diagonal 2')
    else:
        print('Equal')                          
