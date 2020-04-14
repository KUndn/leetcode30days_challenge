class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h = {}
        cur = 0
        maxl = 0
        for i, num in enumerate(nums):
            if num == 0:
                cur -= 1
            else:
                cur += 1
            if cur in h:
                maxl = max(maxl, i - h[cur])
            if cur == 0:
                maxl = max(maxl, i + 1)
            if cur not in h:
                h[cur] = i
        return maxl
        
