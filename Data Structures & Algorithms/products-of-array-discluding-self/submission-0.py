class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for num in nums]

        output = []
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        
        if nums.count(0) == 1:
            return [product if num == 0 else 0 for num in nums]

        return [product // num for num in nums]

        