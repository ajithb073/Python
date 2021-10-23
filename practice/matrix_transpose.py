# 23/20/2021

#transpose 

# 1 2 3     
# 4 5 6
# 7 8 9


# 1 4 7
# 2 5 8
# 3 6 9


#input -> [[1,2,3],[4,5,6],[7,8,9]]

def main():
    mat = input().split()
    mat_row = int(mat[0])
    mat_column = int(mat[1])
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    # for i in range(len(mat)):
    #     # print(i)
    #     result = [[mat[j][i]] for j in range(len(mat))]
    print(result)



# output -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]








# C solution

#include<stdio.h>
int main()
{
	int r, c, mat[10][10], tran[10][10];

	scanf("%d", &r);
	scanf("%d", &c);

	for(int i=0; i<r; i++)
	{
		for(int j=0; j<c; j++)
		{
			scanf("%d", &mat[i][j]);
		}
	}

	for(int i=0; i<r; i++)
	{
		for(int j=0; j<c; j++)
		{
			tran[j][i] = mat[i][j];
		}
	}

for (int i = 0; i<r; ++i)
{ 
  for (int j = 0; j<c; ++j)
   {
        if (j == c - 1)
        printf("%d",tran[i][j]);        
        else           
        printf("%d ",tran[i][j]);  
    }          
       printf("\n"); 
    } return 0;
}
