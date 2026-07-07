class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        numset = {nums[0]}
        for i in range(1,len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
        return False