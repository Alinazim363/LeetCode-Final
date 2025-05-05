class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        longest = 0
        
        for num in counts:
            if (num + 1) in counts:
                length = counts[num] + counts[num + 1]
                if length > longest:
                    longest = length

        return longest   