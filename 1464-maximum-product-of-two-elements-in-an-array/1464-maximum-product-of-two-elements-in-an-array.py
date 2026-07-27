class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=sorted(nums)
        i=a[-1]
        j=a[-2]

        return (i-1)*(j-1)