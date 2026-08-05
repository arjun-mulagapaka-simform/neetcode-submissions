class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        used = set()
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if (nums[i],nums[l],nums[r]) not in used:
                        triplets.append([nums[i],nums[l],nums[r]])
                        used.add((nums[i],nums[l],nums[r]))
                    l += 1
        return triplets