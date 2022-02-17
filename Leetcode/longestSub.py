def longestSub(s):
    dic, res, start, = {}, 0, 0
    for i in range(len(s)):
        if s[i] in dic:
            res = max(res, i - start)  # update the res
            start = max(start, dic[s[i]] + 1)  # here should be careful, like "abba"
        dic[s[i]] = i
    return max(res, len(s) - start)



print(longestSub("dvdfd"))

