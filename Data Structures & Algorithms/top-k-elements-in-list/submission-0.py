class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        
        unique_nums = list(freq.keys())
        sorted_nums = sorted(unique_nums, key=lambda x: freq[x], reverse=True)

        return sorted_nums[:k]
        

        