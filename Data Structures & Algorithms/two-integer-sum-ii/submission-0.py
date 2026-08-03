class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        top, bottom = len(numbers)-1,0
        while bottom < top:
            if numbers[top] + numbers[bottom] > target:
                top -= 1
            elif numbers[top] + numbers[bottom] < target:
                bottom += 1
            else:
                return [bottom+1,top+1]