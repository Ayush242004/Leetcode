class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        b=0
        for num in nums:
            if num==1:
                c+=1
                b=max(c,b)
            else:
                c=0
        return b