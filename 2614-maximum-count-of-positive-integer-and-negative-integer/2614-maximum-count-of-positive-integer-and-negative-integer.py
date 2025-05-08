class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = 0  
        positive = 0 

        for x in nums:
            if x < 0:
                negative += 1
            elif x > 0:
                positive += 1

        if negative > positive:
            return negative
        else:
            return positive          