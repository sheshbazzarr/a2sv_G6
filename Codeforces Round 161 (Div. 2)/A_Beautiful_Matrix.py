matrix = [list(map(int,input().split())) for _ in range(5)]
one_row =-1
one_col=-1
for r in range(5):
    for c in range(5):
        if matrix[r][c]==1:
            one_row=r 
            one_col=c 
            break 
    # this is to exit early it will be true becuase one_row=1 and finding one is guaranted thing 
    if one_row!=-1:
        break 
row_center=2
col_center =2 
row_moves=abs(row_center-one_row)
col_moves=abs(col_center-one_col)
total_moves=row_moves+col_moves
print(total_moves)