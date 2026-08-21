from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = list(set(coins))
        n = len(coins)

        # Precompute (lcm, parity) for every subset
        subsets = []

        for mask in range(1, 1 << n):
            l = 1
            valid = True

            for i in range(n):
                if mask >> i & 1:
                    l = l * coins[i] // gcd(l, coins[i])
                    if l > min(coins) * k:
                        valid = False
                        break

            if valid:
                bits = mask.bit_count()
                subsets.append((l, 1 if bits % 2 else -1))

        def count(x):
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total

        left, right = 1, min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left