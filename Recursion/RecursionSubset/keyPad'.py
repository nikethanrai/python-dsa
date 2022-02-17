
dict = {'1':"",'2': "abc", '3': "def", '4': "ghi", '5': "jkl",'6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
def letterCombinations(Num:str):
    if Num=="":
        return []
    return subset("",Num,[])

def subset(p,up,ans):
    if len(up)==0:
        ans.append(p)
        return
    letters=dict[up[0]]
    for letter in letters:
        subset(p+letter,up[1:],ans)
    return ans
print(letterCombinations("21"))










