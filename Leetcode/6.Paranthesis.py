
def isValid(s):
    a=[]
    dict={'(':')','{':'}','[':']'}
    for i in s:
        print(i)
        if i in dict:
            a.append(i)
            print(a)
        elif len(a)==0 or dict[a.pop()]!=i:
            print(dict[a.pop()])
            return False
    return len(a)==0
print(isValid("()"))


