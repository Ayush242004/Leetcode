class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        arr = []
        for row in grid:
            arr.extend(row)
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]
        ans = []
        for i in range(0, len(arr), n):
            ans.append(arr[i:i+n])
        return ans