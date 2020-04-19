class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self.subsearch(nums, target, 0)
    
    def subsearch(self, nums, target, start):
        if nums[0] == target:
            return start
        if nums[-1] == target:
            return start + len(nums) - 1
        if len(nums) == 1 and nums[0] != target:
            return -1

        midIndex = len(nums) // 2
        leftarr = nums[:midIndex]
        rightarr = nums[midIndex:]

        if leftarr[0] <= target <= leftarr[-1] or (leftarr[-1] < leftarr[0] and (leftarr[0] <= target or target <= leftarr[-1])):
            return self.subsearch(leftarr, target, start)
        else:
            return self.subsearch(rightarr, target, start + midIndex)
