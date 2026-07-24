class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = max(nums) << 1

        pair = [False] * mx
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        seen = [False] * mx
        for x in range(mx):
            if pair[x]:
                for c in nums:
                    seen[x ^ c] = True

        return sum(seen)