class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]:0}
        for i in range(1,len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]],i]
            seen[nums[i]] = i