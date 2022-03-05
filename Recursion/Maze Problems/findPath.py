import np as np

def findPath(p,maze,r,c,x):

    if r==(len(maze)-1) and c==(len(maze[0])-1):
        x.append(p)
        return
    if not maze[r][c]:
        return


    maze[r][c]=False

    if r<(len(maze)-1):
        findPath(p+"D",maze,r+1,c,x)
    if c<(len(maze[0])-1):
        findPath(p+"R",maze,r,c+1,x)
    if r>0:
        findPath(p+"U",maze,r-1,c,x)
    if c>0:
        findPath(p+"L",maze,r,c-1,x)
    maze[r][c]=True


    return (x)
r=3
c=3
bool_arr = np.ones((r,c), dtype=bool)
a=findPath("",bool_arr,0,0,[])
print(a)

print(len(a))
