class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        for i in s:
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i] = 1
        for i in t:
            if i in d1.keys():
                d1[i]=d1[i]+1
            else:
                d1[i] = 1
        if d==d1:
            return True
        else:
            return False
