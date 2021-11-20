ip: 
2 3 4 2
1 4 6 5
4 8 9 6

op:
  Row 3

def main():
    row, col = map(int, input().split())
    mat = []
    for i in range(row):
        mat.append(input().split())
    # print(mat)
    new_mat = [] 
    for rows in mat:
        rows = list(map(int, rows))
        new_mat.append(rows)
    # print(new_mat) 
    list_ind_sum = [sum(i) for i in new_mat] 
    list_sum = max(list_ind_sum)
    max_index = list_ind_sum.index(list_sum)
    print("Row"+" "+str(max_index+1))
