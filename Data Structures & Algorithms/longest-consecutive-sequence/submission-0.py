class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sorted_nums = sorted(set(nums))

        consecutive_seq = 1
        longest_consecutive_seq = 1
        prev_num = sorted_nums[0]
        
        for num in sorted_nums:
            if num == prev_num + 1:
                consecutive_seq += 1
            else:
                consecutive_seq = 1
            
            longest_consecutive_seq = max(consecutive_seq, longest_consecutive_seq)

            prev_num = num
        
        return longest_consecutive_seq




        