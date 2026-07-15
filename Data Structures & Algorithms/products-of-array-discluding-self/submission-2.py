from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for _ in range(len(nums))]
        suffix_prod = nums[-1]
        prefix_prods = [1]
        for i in range(1,len(nums)):
            prefix_prods.append(nums[i-1]*prefix_prods[i-1])
        for i in range(len(nums)-2,-1,-1):
            output[i] = prefix_prods[i]*suffix_prod
            suffix_prod *= nums[i]
        output[-1] = prefix_prods[-1]
        return output