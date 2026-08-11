class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_max = [0 for _ in range(len(height))]
        suffix_max[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            suffix_max[i] = max(height[i],suffix_max[i+1])
        
        prefix_max,total = 0,0
        for i in range(len(height)):
            prefix_max = max(prefix_max,height[i])
            total += min(prefix_max,suffix_max[i]) - height[i]
        
        return total