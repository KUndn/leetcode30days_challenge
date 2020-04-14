 def moveZeroes(self, nums: List[int]) -> None:
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                a=nums.pop(i)
                nums.insert(count,a)
                count+=1
            else:
                continue
