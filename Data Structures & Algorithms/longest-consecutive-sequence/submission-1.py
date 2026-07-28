class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq = 0
        for i in set_nums:
            if i-1 not in set_nums:
                num = i
                curr_seq = 1
                while num+1 in set_nums:
                    num += 1
                    curr_seq += 1
                max_seq = max(max_seq,curr_seq)

        return max_seq