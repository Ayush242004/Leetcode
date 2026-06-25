from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        arr = [1 if x == target else -1 for x in nums]

        prefix = [0]
        for x in arr:
            prefix.append(prefix[-1] + x)

        vals = sorted(set(prefix))

        bit = Fenwick(len(vals))
        ans = 0

        for p in prefix:
            rank = bisect_left(vals, p) + 1
            ans += bit.query(rank - 1)
            bit.update(rank, 1)

        return ans