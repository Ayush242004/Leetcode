class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        ans = ""
        for right in range(len(s)):
            if s[right] == '1':
                count += 1
            while count == k:
                curr = s[left:right + 1]
                if ans == "" or len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans) and curr < ans:
                    ans = curr
                if s[left] == '1':
                    count -= 1

                left += 1

        return ans