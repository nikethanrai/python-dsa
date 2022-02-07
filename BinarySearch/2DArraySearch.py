def ArraySearch(arr,Num):
    row=0
    col=len(arr[0])-1
    while row<len(arr) and col>=0:
        if arr[row][col]==Num:
            return(row,col)
        if arr[row][col]<Num:
            row+=1
        else:
            col-=1
    return (-1,-1)

print(ArraySearch([[1,2],[4,5],[7,9]],21))
