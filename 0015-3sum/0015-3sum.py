class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=set()
        for i in range(0,len(nums)):
            myset=set()
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if third in myset:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    ans.add(tuple(temp))
                myset.add(nums[j])
        return [list(x)for x in ans]