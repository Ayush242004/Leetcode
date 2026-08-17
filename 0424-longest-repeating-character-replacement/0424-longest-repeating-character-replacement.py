class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        res=0
        mf=0
        l=0
        ml=0
        for r in range(len(s)):

            c[s[r]] = 1 + c.get(s[r], 0)
            mf = max(mf, c[s[r]])
            while (r - l + 1) - mf > k:
                c[s[l]] -= 1  
                l += 1
            ml = max(ml, r - l + 1)
        return ml