matrix =[list(map(int,input().split())) for _ in range(5)]

# find postion of '1'
one_row ,one_col=-1,-1
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            one_row,one_col=i,j
            break 
    if one_row!=-1:
        break 
center_row,center_col=2,2
row_moves =abs(one_row-center_row)
col_moves=abs(one_col-center_col)

total_moves=row_moves+col_moves 

print(total_moves)