from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_prods = [1]
        suffix_prods = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(0,i):
        #         prod *= nums[j]
        #     for k in range(i+1,len(nums)):
        #         prod *= nums[k]
        #     output.append(prod)
        prefix_prod = 1
        suffix_prod = 1
        for i in range(1,len(nums)):
            prefix_prods.append(reduce(lambda x,y: x*y, nums[:i]))
        for i in range(0,len(nums)-1):
            suffix_prods.append(reduce(lambda x,y: x*y, nums[i+1:]))
        suffix_prods.append(1)
        for i in range(0,len(nums)):
            output.append(prefix_prods[i]*suffix_prods[i])
        return output