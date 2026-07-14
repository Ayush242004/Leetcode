class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        n=num+1
        return [int(d) for d in str(n)]