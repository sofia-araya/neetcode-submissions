class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        
        longest_consecutive_seq = 1

        for num in nums_set:
            consecutive_seq = 1
            if num-1 not in nums_set:
                while num + consecutive_seq in nums_set:
                    consecutive_seq +=1

            longest_consecutive_seq = max(longest_consecutive_seq, consecutive_seq)
        
        return longest_consecutive_seq
        




        