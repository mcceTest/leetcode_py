def KMPSearch(s, p):
    '''
    @param s: string to be searched
    @param p: string pattern to search s
    @return: array of indices of s where p starts
    '''
    res = []
    if not s or not p:
        return res

    lps = findKMPArray(s) 
    sIdx = pIdx = 0
    while sIdx < len(s):
        if s[sIdx] == p[pIdx]:
            sIdx += 1
            pIdx += 1
            # find a match
            if pIdx == len(p):
                res.append(sIdx - len(p))
                pIdx = lps[pIdx - 1]
        else:
            # not match at beginning
            if pIdx == 0:
                sIdx += 1
            else:
                pIdx = lps[pIdx - 1]

    return res

def findKMPArray(s):
    '''
    Longest length of a prefix of a sub string of s ending at index i, which is also sufixx of the sub string.
    aka. longest proper prefix
    '''
    lps = [0] * len(s)
    for i in range(1, len(s)):
        preLen = lps[i - 1]
        foundMatch = True
        while s[i] != s[preLen]:
            if preLen == 0:
                ## can not find any match. default length is 0
                foundMatch = False
                break
            else:
                preLen = lps[preLen - 1]
        if foundMatch:
            lps[i] = preLen + 1

    return lps

if __name__ == "__main__":
    s = "ABCABD"

    print(KMPSearch(s, "A"))    
        
