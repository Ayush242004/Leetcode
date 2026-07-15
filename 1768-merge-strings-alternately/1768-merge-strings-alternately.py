class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        a=len(word1)
        b=len(word2)
        while a>0 and b>0:
            s+=word1[len(word1)-a]
            s+=word2[len(word2)-b]
            a-=1
            b-=1
        while a>0:
            s+=word1[len(word1)-a]
            a-=1
        while b>0:
            s+=word2[len(word2)-b]
            b-=1
        return s